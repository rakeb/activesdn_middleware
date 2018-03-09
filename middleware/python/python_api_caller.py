from api.handler import api_handler

cnt = 1
event_output = None
action_spec_output = None
coa_output = None


def call_api(node):
    global cnt
    global event_output
    global action_spec_output
    global coa_output

    p_all_nodes = node.children
    if node.name == 'rule':
        label = 'rule_' + str(cnt)
        event = call_api(p_all_nodes[0])
        coa = call_api(p_all_nodes[1])
        # write_prolog_line('rule(%s, %s, %s).' % (label, event, coa))
        return label
    elif node.name == 'event':
        label = 'evt_' + str(cnt)
        api_handler.handle_event(node.body)
        # write_prolog_line('event(%s, %s).' % (label, node.body))
        return label
    elif node.name == 'op':
        # Add support to have operation with more than two operands
        # opType = opDict[node.body]
        left = call_api(p_all_nodes[0])
        right = call_api(p_all_nodes[1])
        label = 'op_' + str(cnt)
        cnt += 1
        # write_prolog_line('coa(%s, %s, %s, %s).' % (label, opType, left, right))
        return label
    elif node.name == 'action_spec':
        # write_prolog_line(node.pFact)
        return node.id
    elif node.name == 'if_node':
        label = 'if_' + str(cnt)
        cnt += 1
        condition = node.body
        # if len(p_all_nodes) > 0:
        # We should have only one child for this node
        # Retrieve its ID
        thenNode = call_api(p_all_nodes[0])
        # if len(p_all_nodes) > 1:
        elseNode = call_api(p_all_nodes[1])
        coa_if = 'coa_if(%s, %s, %s, %s).' % (label, condition, thenNode, elseNode)
        # write_prolog_line(coa_if)
        return label

    else:
        for child in p_all_nodes:
            call_api(child)


if __name__ == '__name__':
    call_api(rule=None)
