from pyparsing import Word, nums, alphas, alphanums, Forward, delimitedList, Group, oneOf, srange, Optional, OneOrMore, \
    Combine, ZeroOrMore

from policy.parser.parsePythonValue import (integer, real, dictStr as dict_literal,
                                            listStr as list_literal, tupleStr as tuple_literal, lparen, rparen)


# -*- coding: utf-8 -*-
def policy_parser():
    if_s = 'IF (DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command ' \
           'FOR PREVENT OUTCOME O1) THEN DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> ' \
           'USING deny-command FOR PREVENT OUTCOME O2 '
    elseif_s = 'ELSEIF (DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT OUTCOME O3) THEN DO Block ON flows  OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT OUTCOME O4 '
    e_s = 'ELSE DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> ' \
          'USING deny-command FOR PREVENT OUTCOME O5'

    # defines ip_address
    ip_address = Word(nums) + ('.' + Word(nums)) * 3

    # defines identifier
    underscore_id = Word(alphas + '_', alphanums + '_')
    dashed_id = Word(alphas + '-', alphanums + '-')
    identifier = dashed_id ^ underscore_id
    # print(identifier.parseString('src-ip'))


    # defines comparision
    comp_oper = oneOf("< = > <= >= != ∉ ∈ <> ∅")
    # number = Word(nums)
    percent_number = Word(nums, nums + '%')
    term = '∅' | percent_number | identifier
    comparison_expr = term + comp_oper + term
    # print(comparison_expr.parseString('E <> ∅'))

    # define a func_call
    func_call = Forward()
    arg_expr = identifier | real | integer | dict_literal | list_literal | tuple_literal | func_call
    named_arg = identifier + '=' + arg_expr
    func_arg = named_arg | ip_address | arg_expr
    # print(delimitedList(Group(func_arg)).parseString('l, t'))

    func_call << identifier + '(' + Optional(delimitedList(Group(func_arg))) + ')'
    # print(func_call.parseString('Link-Flooded() '))

    # ActiveSDN Policy BNF

    # using rate > 50%
    operator = oneOf('OR or ; || && ->')
    weight = srange(1 - 10)
    action_attribution = delimitedList(Group(comparison_expr)) | identifier
    # print(action_attribution.parseString('rate > 50%'))

    # BY IDS - App
    # BY Switch < 1.1.1.1 >
    # BY FIREWALL < 1.5.6.4, “admin” >
    as_using_param = identifier + '<' + delimitedList(Group(func_arg)) + '>'
    actuator_spec = identifier ^ delimitedList(Group(as_using_param))
    # print(actuator_spec.parseString('IDS-App'))
    # print(actuator_spec.parseString('Switch < 1.1.1.1 >'))
    # print(actuator_spec.parseString('FIREWALL < 1, admin >'))

    # Object = oneOf('files flows links machines')
    object = identifier
    fw__actions = oneOf('ACCEPT DENY REDIRECT')
    snmp_get_action = identifier
    log_audit_action = identifier
    splunk_action = identifier
    camera_actions = identifier
    ids_actions = identifier
    ipsec_action = identifier
    proxy_action = identifier

    investigation_action = snmp_get_action | log_audit_action | splunk_action | camera_actions
    config_action = fw__actions | ids_actions | ipsec_action | proxy_action

    action = config_action | investigation_action

    outcome_value = delimitedList(func_arg) + operator + comparison_expr
    value = delimitedList(Group(outcome_value)) | identifier
    # print(Value.parseString('P,l  && P <> 0'))

    # OF(proto=CIMP or UDP in P)
    # OF E
    # OF(src_ip ∈ N)
    # OF(src_ip ∈ WHITE - LIST)
    # OF src_ip ∉ W
    multiple_flow_attributes = func_arg + operator + identifier
    single_flow_attribute = func_arg | identifier
    flow_attributes = multiple_flow_attributes | single_flow_attribute

    # OF(Reachable(L) and dport = 80)
    link_attributes = func_call + operator + func_arg | func_call | func_arg | identifier
    # print(link_attributes.parseString('Reachable(L) && dport = 80'))

    # TODO we will define them later
    file_attributes = identifier
    machine_attributes = identifier

    attributes = flow_attributes ^ file_attributes ^ link_attributes ^ machine_attributes
    attribute_values = ZeroOrMore(lparen) \
                       + (comparison_expr ^ (attributes + 'in' + identifier) ^ attributes ^ identifier) \
                       + ZeroOrMore(rparen)
    obj_attribute_values = delimitedList(Group(attribute_values))
    # print(obj_attribute_values.parseString('(Reachable(L) && dport = 80)'))

    keyword = oneOf('DO ON OF BY USING FOR OUTCOME UNTIL')
    goal = identifier
    event_exp = Forward()
    do_action = 'DO' + action
    on_object = 'ON' + object
    of_obj_attribute_values = 'OF' + obj_attribute_values
    by_actuator_spec = 'BY' + actuator_spec
    using_action_attribution = 'USING' + action_attribution
    for_goal = 'FOR' + goal
    outcome_value = 'OUTCOME' + value

    # action_spec = Optional('DO' + action) + Optional('ON' + object) + Optional(
    #     'OF' + obj_attribute_values) + Optional('BY' + actuator_spec) + \
    #               Optional('USING' + action_attribution) + Optional('FOR' + goal) + Optional(
    #     'OUTCOME' + value)

    action_spec = do_action + Optional(on_object) + Optional(of_obj_attribute_values) + Optional(
        by_actuator_spec) + Optional(using_action_attribution) + Optional(for_goal) + outcome_value

    # action_spec = 'DO' + action + 'ON' + object + 'OF' + obj_attribute_values + 'BY' + actuator_spec + 'USING' \
    #               + action_attribution + 'FOR' + goal
    #               # + 'OUTCOME' + value

    # action_spec = 'DO' + action + 'ON' + object + 'OF' + obj_attribute_values + 'BY' + actuator_spec + 'USING' \
    #               + action_attribution + 'FOR' + goal
    # + 'OUTCOME' + value

    # print(action_spec.parseString(
    #     'DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT'))

    # + Optional('UNTIL' + event__exp)
    # action_spec = identifier
    coas = Forward()
    coas << (ZeroOrMore(lparen) + (Group(delimitedList(action_spec)) + operator + coas) + ZeroOrMore(rparen)
             | Group(delimitedList(action_spec)))

    # coas << (Optional('(') + (Group(delimitedList(action_spec)) + operator + coas) + Optional(')')
    #          | Optional('(') + Group(delimitedList(action_spec))) + Optional(')')
    # | (Group(delimitedList(coas))) + operator + Group(delimitedList(coas)))

    # print(coas.parseString(
    #     'DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% OUTCOME P && P <> ∅'))
    #  print(coas.parseString(
    #     'DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT'))
    # out_coas = coas.parseString(
    #     'DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT '
    #     'OR DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT')
    # for s in out_coas:
    #     print(s)

    # COA SPEC
    # ca_spec = (Optional('ELSE') + 'IF' + Optional(OneOrMore(lparen)) + coas + Optional(OneOrMore(rparen)) + 'THEN' + coas) | ('ELSE' + coas) | coas
    ca_spec = coas | 'IF' + ZeroOrMore(lparen) + coas + ZeroOrMore(rparen) + 'THEN' + coas | 'ELSE IF' + ZeroOrMore(
        lparen) + coas + ZeroOrMore(rparen) + 'THEN' + coas | 'ELSE' + coas

    # ca_spec = Optional('ELSE') + 'IF' + lparen + coas + rparen + 'THEN' + coas | 'ELSE' + coas
    coas_spec = Group(delimitedList(ca_spec))
    short_policy = if_s + elseif_s + e_s
    # print(coas_spec.parseString(short_policy))
    # print(ca_spec.parseString(elseif_s))
    # print(coas_spec.parseString("ELSE IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% OUTCOME P && P <> ∅) THEN DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT OUTCOME o"))
    #
    # print(coas_spec.parseString(
    #     'DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT'))
    # out_coas = coas_spec.parseString(
    #     'DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT '
    #     'OR DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT')
    # for s in out_coas:
    #     print(s)

    #
    # print(coas_spec.parseString(
    #         'DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT'))
    # out_coas = coas_spec.parseString(
    #     'DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT '
    #     'OR DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT')
    # for s in out_coas:
    #     print(s)

    # a = ZeroOrMore(lparen) + ZeroOrMore(coas_spec) + ZeroOrMore(rparen)
    # print(a.parseString(short_policy))
    # coas_spec = Group(delimitedList(ca_spec))

    # coas_spec = Forward()
    # if_then_else = Optional('IF') + Optional(OneOrMore(lparen)) + coas + Optional(OneOrMore(rparen)) + \
    #                'THEN' + coas + "ELSE" + coas
    # coas_spec << (coas ^ if_then_else)
    # coas_spec << (('IF' + coas + 'THEN' + coas_spec + oneOf('ELSE ELSEIF') + coas_spec) | coas)
    # coas_spec << (('IF' + Optional(OneOrMore(lparen)) + Group(delimitedList(coas)) + Optional(OneOrMore(rparen)) +
    #                'THEN' + coas_spec + Optional(OneOrMore('ELSE' + coas_spec)) + 'ELSE' +
    #                coas_spec | Group(delimitedList(coas))))

    # print(coas_spec.parseString(if_s + elseif_s + e_s))
    # print(coas_spec.parseString(if_s + elseif_s + e_s))
    # print(coas_spec.parseString(short_policy))
    # print(if_then_else.parseString(short_policy))


    # print(coas_spec.parseString(
    #     'IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% OUTCOME P && P <> ∅) THEN DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT'))
    #
    # print(coas_spec.parseString(
    #     'ELSE IF (DO CheckElephantTCPFlow ON flows BY IDS-App USING rate  > 90% FOR DETECT OUTCOME E && E <> ∅) THEN DO Block ON flows OF E BY FIREWALL<1.5.6.4, admin> USING deny-command FOR PREVENT'))
    #
    # print(coas_spec.parseString(
    #     'IF (DO CheckNewComers ON flows BY IDS-App USING window < 1 OUTCOME N, rate && rate > 75%) THEN DO Rereoute ON flows OF (src_ip ∈ N) BY ROUTER USING RRM<>'))
    #
    # print(coas_spec.parseString(
    #     'ELSE DO Replicate ON services OF (Reachable(L) && dport=80) USING replicate-command  DO Reroute ON flows  OF USING Switch'))
    #
    # print(coas_spec.parseString(
    #     'ELSE  DO Reroute ON flows USING Switch'))
    #
    # print(coas_spec.parseString(
    #     'IF (DO CheckNewComers ON flows BY IDS-App USING window < 1 OUTCOME N, rate && rate > 75%) THEN DO Rereoute ON flows OF (src_ip ∈ N) BY ROUTER USING RRM ELSE DO Reroute ON flows USING Switch'))
    #
    # print(coas_spec.parseString(if_s))
    # print(coas_spec.parseString(elseif_s))
    # a = Optional(lparen) + ZeroOrMore(coas_spec) + Optional(rparen)
    # print(a.parseString(
    #     '(IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% OUTCOME P && P <> ∅) THEN DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT '
    #     'ELSE IF (DO CheckElephantTCPFlow ON flows BY IDS-App USING rate  > 90% FOR DETECT OUTCOME E && E <> ∅) THEN DO Block ON flows OF E BY FIREWALL<1.5.6.4, admin> USING deny-command FOR PREVENT '
    #     'ELSE DO Replicate ON services OF (Reachable(L) && dport=80) USING replicate-command  '
    #     'ELSE DO Reroute ON flows USING Switch)'
    # ))

    temp_context_exp = func_call
    config_context_exp = func_call
    dynamic_context_exp = func_call
    context_exp = Group(temp_context_exp | config_context_exp | dynamic_context_exp).setName('exp')

    rule = ZeroOrMore(lparen) + context_exp + ZeroOrMore(rparen) + operator + ZeroOrMore(coas_spec)
    # print(rule.parseString(
    #     'Link-Flooded(T,L) -> ELSE IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% OUTCOME P && P <> ∅) THEN DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT OUTCOME o'))

    # parsed_policy = rule.parseString(
    #     '(Link-Flooded(T,L)) -> '
    #         'IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% '
    #             'OUTCOME P && P <> ∅) THEN '
    #                 'DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> '
    #                 'USING deny-command FOR PREVENT '
    #         'ELSE IF (DO CheckElephantTCPFlow ON flows BY IDS-App USING rate>90% '
    #             'FOR DETECT OUTCOME E && E <> ∅) THEN '
    #                 'DO Block ON flows OF E BY FIREWALL <1.5.6.4, admin> '
    #                 'USING deny-command FOR PREVENT '
    #         'ELSE '
    #             'DO Replicate ON services OF (Reachable(L) && dport=80) USING replicate-command  '
    # )
    # for rule in parsed_policy:
    #     print(rule)

    policy_string = ''
    with open('policy_1.txt') as f:
        content = f.read()
        policy_string += content

        print(policy_string)

        parsed_policy = rule.parseString(policy_string)
        for rule in parsed_policy:
            print(rule)


if __name__ == '__main__':
    policy_parser()
