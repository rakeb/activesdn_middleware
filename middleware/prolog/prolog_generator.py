f = None
cnt = 1

opDict = {
    '||': 'par',
    ';': 'seq'
}


def write_prolog_line(l):
    global f
    f.write(l)
    f.write("\n")


def write_prolog_header():
    write_prolog_line('op(seq).')
    write_prolog_line('op(par).')


def write_prolog_rules():
    isCoa = '''isCoa(X):-
	action_spec(X,_,_,_,_,_,_,_);
	coa_if(X,_,Then,Else), isCoa(Then), isCoa(Else);
	coa(X, OP, L, R), isCoa(L), isCoa(R), op(OP).'''

    write_prolog_line(isCoa)

    isRule = '''isRule(X):-
    rule(X, Event, Op_Id),
    event(Event,_),
    isCoa(Op_Id).'''

    write_prolog_line(isRule)

    isEqual = '''isEqual(X, Y):-
	subtract(X,Y,[]),
	subtract(Y,X,[]).'''

    write_prolog_line(isEqual)
    isRedundant = '''isRedundant(X,Y):-
        action_spec(X, Action_X, Objects_X, Object_Atrb_X, Actuator_X, _, _, _),
        action_spec(Y, Action_Y, Objects_Y, Object_Atrb_Y, Actuator_Y, _, _, _),
        isEqual(Actuator_X, Actuator_Y),
        Objects_X == Objects_Y,
        isEqual(Object_Atrb_X, Object_Atrb_Y),
		Action_X == Action_Y.'''
    write_prolog_line(isRedundant)

    isPermanentAccessconflict = '''isPermanentAccessconflict(X,Y):-
        action_spec(X, Action_X, Objects_X, Object_Atrb_X, Actuator_X, _, _, _),
        action_spec(Y, Action_Y, Objects_Y, Object_Atrb_Y, Actuator_Y, _, _, _),
        %isEqual(Actuator_X, Actuator_Y),
        Objects_X == Objects_Y,
        isEqual(Object_Atrb_X, Object_Atrb_Y),
		Action_X \= Action_Y.'''
    write_prolog_line(isPermanentAccessconflict)

    isShadowing = '''isShadowing(X,Y):-
        action_spec(X, Action_X, Objects_X, Object_Atrb_X, Actuator_X, _, _, _),
        action_spec(Y, Action_Y, Objects_Y, Object_Atrb_Y, Actuator_Y, _, _, _),
        not(isEqual(Actuator_X, Actuator_Y)),
        (Objects_X \= Objects_Y;
        not(isEqual(Object_Atrb_X, Object_Atrb_Y))),
		Action_X \= Action_Y.'''
    write_prolog_line(isShadowing)


    isConflict = '''isConflict(X,Y,O):-
            isRedundant(X,Y) -> write("Redundant (Sequential actions? Different rules? Action-level?)");
            isPermanentAccessconflict(X,Y) -> write("Permanent Access conflict: searilizability and consistency check (files or flows) on different switches have different action -> Action: select one actuator/action only  or give a priororty");
            isShadowing(X,Y) -> write("Rule Shadowing");
            write("No Conflict!"), false.'''
    write_prolog_line(isConflict)


def generate_prolog(node):
    global cnt
    thenNode = None
    elseNode = None
    p_all_nodes = node.children
    if node.name == 'op':
        # Add support to have operation with more than two operands
        opType = opDict[node.body]
        left = generate_prolog(p_all_nodes[0])
        right = generate_prolog(p_all_nodes[1])
        label = 'op_' + str(cnt)
        cnt += 1
        write_prolog_line('coa(%s, %s, %s, %s).' % (label, opType, left, right))
        return label
    elif node.name == 'action_spec':
        write_prolog_line(node.pFact)
        return node.id
    elif node.name == 'if_node':
        label = 'if_' + str(cnt)
        cnt += 1
        condition = node.body
        # if len(p_all_nodes) > 0:
        # We should have only one child for this node
        # Retrieve its ID
        thenNode = generate_prolog(p_all_nodes[0])
        # if len(p_all_nodes) > 1:
        elseNode = generate_prolog(p_all_nodes[1])
        coa_if = 'coa_if(%s, %s, %s, %s).' % (label, condition, thenNode, elseNode)
        write_prolog_line(coa_if)
        return label
    elif node.name == 'rule':
        label = 'rule_' + str(cnt)
        event = generate_prolog(p_all_nodes[0])
        coa = generate_prolog(p_all_nodes[1])
        write_prolog_line('rule(%s, %s, %s).' % (label, event, coa))
        return label
    elif node.name == 'event':
        label = 'evt_' + str(cnt)
        write_prolog_line('event(%s, %s).' % (label, node.body))
        return label
    else:
        for child in p_all_nodes:
            generate_prolog(child)


def generate_prolog_file(rule, fname):
    global f
    f = open(fname, "w")
    write_prolog_header()
    generate_prolog(rule)
    write_prolog_rules()
    f.close()


if __name__ == '__main__':
    generate_prolog_file(rule=None, fname="prolog.pl")
