from api.handler import api_handler

cnt = 1
event_output = None
action_spec_output = None
coa_output = None
rule = None
activesdn_response = None


def call_event_api(node):
    global cnt
    global event_output

    p_all_nodes = node.children
    if node.name == 'rule':
        label = 'rule_' + str(cnt)
        event = call_event_api(p_all_nodes[0])
        # coa = call_event_api(p_all_nodes[1])
        # write_prolog_line('rule(%s, %s, %s).' % (label, event, coa))
        return label
    elif node.name == 'event':
        # label = 'evt_' + str(cnt)
        event_output = api_handler.handle_event(node.body)
        # write_prolog_line('event(%s, %s).' % (label, node.body))
        # return label
        return event_output
    else:
        for child in p_all_nodes:
            call_event_api(child)


def call_coa_api(node):
    global cnt
    global action_spec_output
    global coa_output
    global activesdn_response

    p_all_nodes = node.children
    if node.name == 'rule':
        label = 'rule_' + str(cnt)
        coa = call_coa_api(p_all_nodes[1])
        return label
    elif node.name == 'op':
        # Add support to have operation with more than two operands
        left = call_coa_api(p_all_nodes[0])
        right = call_coa_api(p_all_nodes[1])
        return left
    elif node.name == 'action_spec':
        action_spec_output = api_handler.handle_action_spec(node, action_spec_output, activesdn_response)
        return action_spec_output
    elif node.name == 'if_node':
        decision = api_handler.handle_if_condition(node, action_spec_output)
        tf_then = None
        if decision:
            tf_then = call_coa_api(p_all_nodes[0])
        else:
            tf_then = call_coa_api(p_all_nodes[1])
        return tf_then

    else:
        for child in p_all_nodes:
            call_coa_api(child)


def coa_caller(rule, response):
    global activesdn_response
    activesdn_response = response
    call_coa_api(rule)


def event_caller(p_rule):
    global rule
    rule = p_rule
    call_event_api(rule)


if __name__ == '__name__':
    # call_api(rule=None)
    pass
