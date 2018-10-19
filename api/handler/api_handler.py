from api.impl import ActiveSdnServiceImpl


def call_link_flooding_api():
    output = ActiveSdnServiceImpl.findPotentialFloodedLink()

    print("from api handler, printing SDN Response: ", output)

    leftSwitch = output['output']['left-switch']
    leftSwitchPort = output['output']['left-switch-port']
    criticalLink = [int(n) for n in output['output']['criticalLink'].split(':')]
    drop_threshold = 1

    ActiveSdnServiceImpl.subscribeForStatsFromSwitch(criticalLink)
    ActiveSdnServiceImpl.subscribeForLinkFloodingCheck(leftSwitch, leftSwitchPort, drop_threshold)
    return output


def handle_event(body):
    if body[0] == 'Link-Flooded':
        return call_link_flooding_api()


def remove_percent_sign_if_contains(condition):
    return int(condition.split('%')[0])


def call_check_udp_icmp_flows_api(actionSpec, activesdn_response):
    switch_id = int(activesdn_response.split(':')[1])
    condition = actionSpec.usingAttribute.condition
    anomalous_rate = remove_percent_sign_if_contains(condition)
    output = ActiveSdnServiceImpl.checkUdpIcmpFlows(switch_id, anomalous_rate)
    ret_value = None
    if len(output['output'].keys()) == 0:
        ret_value = []
    else:
        ret_value = output['output']['flow-ids']
    return ret_value


def call_block_api(actionSpec, preCondition, activesdn_response):
    list_proto = actionSpec.ofAttribute.value
    proto = None
    if 'UDP' in list_proto:
        proto = 'UDP'
    elif 'TCP' in list_proto:
        proto = 'Elephant'

    switch_id = int(activesdn_response.split(':')[1])

    for flow_id in preCondition:
        output = ActiveSdnServiceImpl.blockFlow(switch_id, flow_id, proto)

    return output['output']


def call_check_elephant_tcp_flow_api(actionSpec, activesdn_response):
    switch_id = int(activesdn_response.split(':')[1])
    condition = actionSpec.usingAttribute.condition
    anomalous_threshold = remove_percent_sign_if_contains(condition)
    output = ActiveSdnServiceImpl.checkElephantTcpFlow(switch_id, anomalous_threshold)
    ret_value = None
    if len(output['output'].keys()) == 0:
        ret_value = []
    else:
        ret_value = output['output']['flow-ids']
    return ret_value


def handle_action_spec(actionSpec, preCondition, activesdn_response):
    if actionSpec.doAttribute == 'CheckUDPICMPFlows':
        return call_check_udp_icmp_flows_api(actionSpec, activesdn_response)
    elif actionSpec.doAttribute == 'CheckElephantTCPFlow':
        return call_check_elephant_tcp_flow_api(actionSpec, activesdn_response)
    elif actionSpec.doAttribute == 'Block':
        return call_block_api(actionSpec, preCondition, activesdn_response)
    else:
        exceptionString = 'NoSuchFunctionException: %s' % (actionSpec.doAttribute)
        raise Exception(exceptionString)


def handle_if_condition(if_node, preCondition):
    operator = if_node.operator
    condition = remove_percent_sign_if_contains(if_node.condition)
    if not if_node.isUniary:
        if operator == '<>':
            if isinstance(preCondition, list):
                if len(preCondition) != condition:
                    return True
            else:
                if preCondition != condition:
                    return True
        elif operator == '=':
            if preCondition == condition:
                return True
        elif operator == '>':
            if preCondition > condition:
                return True
        elif operator == '<':
            if preCondition < condition:
                return True
    return False


    # checkUdpIcmpFlows(1, 20)
    # blockFlow(1, '115', 'UDP')
    # checkElephantTcpFlow(1, 4)
