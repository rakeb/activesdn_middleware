from pyparsing import Word, nums, alphas, alphanums, Forward, delimitedList, Group, oneOf, srange, Optional, OneOrMore

from policy.parser.parsePythonValue import (integer, real, dictStr as dict_literal,
                                            listStr as list_literal, tupleStr as tuple_literal, lparen, rparen)


# -*- coding: utf-8 -*-
def policy_parser():
    # defines ipAddress
    ipAddress = Word(nums) + ('.' + Word(nums)) * 3

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
    func_arg = named_arg | ipAddress | arg_expr
    # print(delimitedList(Group(func_arg)).parseString('l, t'))

    func_call << identifier + '(' + Optional(delimitedList(Group(func_arg))) + ')'
    # print(func_call.parseString('Link-Flooded() '))

    # ActiveSDN Policy BNF
    Operator = oneOf('OR or ; || && ->')
    weight = srange(1 - 10)
    ActionAttribution = delimitedList(Group(comparison_expr)) | identifier

    # BY IDS - App
    # BY Switch < 1.1.1.1 >
    # BY FIREWALL < 1.5.6.4, “admin” >
    as_using_param = identifier + '<' + delimitedList(Group(func_arg)) + '>'
    Actuator_spec = identifier ^ delimitedList(Group(as_using_param))
    # print(Actuator_spec.parseString('FIREWALL < 1, admin >'))

    # Object = oneOf('files flows links machines')
    Object = identifier
    FW_Actions = oneOf('ACCEPT DENY REDIRECT')
    SNMPGetAction = identifier
    LogAuditAction = identifier
    SplunkAction = identifier
    CameraActions = identifier
    IDSActions = identifier
    IPSecAction = identifier
    ProxyAction = identifier
    InvestigationAction = SNMPGetAction | LogAuditAction | SplunkAction | CameraActions
    ConfigAction = FW_Actions | IDSActions | IPSecAction | ProxyAction
    Action = ConfigAction | InvestigationAction

    outcome_value = delimitedList(func_arg) + Operator + comparison_expr
    Value = delimitedList(Group(outcome_value)) | identifier
    # print(Value.parseString('P,l  && P <> 0'))

    # OF(proto=CIMP or UDP in P)
    # OF E
    # OF(src_ip ∈ N)
    # OF(src_ip ∈ WHITE - LIST)
    # OF src_ip ∉ W
    multiple_flow_attributes = func_arg + Operator + identifier
    single_flow_attribute = func_arg | identifier
    FlowAttributes = multiple_flow_attributes | single_flow_attribute

    # OF(Reachable(L) and dport = 80)
    LinkAttributes = func_call + Operator + func_arg | func_call | func_arg | identifier
    # print(LinkAttributes.parseString('Reachable(L) && dport = 80'))

    # TODO we will define them later
    FileAttributes = identifier
    MachineAttributes = identifier

    Attributes = FlowAttributes ^ FileAttributes ^ LinkAttributes ^ MachineAttributes
    attribute_values = Optional(lparen) + (
        comparison_expr ^ (Attributes + 'in' + identifier) ^ Attributes ^ identifier) + Optional(
        rparen)
    ObjAttributeValues = delimitedList(Group(attribute_values))
    # print(ObjAttributeValues.parseString('(Reachable(L) && dport = 80'))

    keyword = oneOf('DO ON OF BY USING FOR OUTCOME UNTIL')
    Goal = identifier
    Event_Exp = Forward()
    Action_spec = Optional('DO' + Action) + Optional('ON' + Object) + Optional(
        'OF' + ObjAttributeValues) + Optional('BY' + Actuator_spec) + \
                  Optional('USING' + ActionAttribution) + Optional('FOR' + Goal) + Optional(
        'OUTCOME' + Value)
    # + Optional('UNTIL' + Event_Exp)
    CoAs = Action_spec

    # if_then_else = oneOf('')

    ca_spec = Optional('ELSE') + 'IF' + lparen + CoAs + rparen + 'THEN' + CoAs | 'ELSE' + CoAs
    CoAs_Spec = Group(delimitedList(ca_spec))

    if_s = 'IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% OUTCOME P && P <> ∅) THEN DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT'
    elseif_s = 'ELSE IF (DO CheckElephantTCPFlow ON flows BY IDS-App USING rate  > 90% FOR DETECT OUTCOME E && E <> ∅) THEN DO Block ON flows OF E BY FIREWALL<1.5.6.4, admin> USING deny-command FOR PREVENT'
    e_s = 'ELSE DO Replicate ON services OF (Reachable(L) && dport=80) USING replicate-command  DO Reroute ON flows  OF USING Switch'

    # print(CoAs_Spec.parseString(
    #     'IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% OUTCOME P && P <> ∅) THEN DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT'))
    #
    # print(CoAs_Spec.parseString(
    #     'ELSE IF (DO CheckElephantTCPFlow ON flows BY IDS-App USING rate  > 90% FOR DETECT OUTCOME E && E <> ∅) THEN DO Block ON flows OF E BY FIREWALL<1.5.6.4, admin> USING deny-command FOR PREVENT'))
    #
    # print(CoAs_Spec.parseString(
    #     'IF (DO CheckNewComers ON flows BY IDS-App USING window < 1 OUTCOME N, rate && rate > 75%) THEN DO Rereoute ON flows OF (src_ip ∈ N) BY ROUTER USING RRM<>'))
    #
    # print(CoAs_Spec.parseString(
    #     'ELSE DO Replicate ON services OF (Reachable(L) && dport=80) USING replicate-command  DO Reroute ON flows  OF USING Switch'))
    #
    # print(CoAs_Spec.parseString(
    #     'ELSE  DO Reroute ON flows USING Switch'))
    #
    # print(CoAs_Spec.parseString(
    #     'IF (DO CheckNewComers ON flows BY IDS-App USING window < 1 OUTCOME N, rate && rate > 75%) THEN DO Rereoute ON flows OF (src_ip ∈ N) BY ROUTER USING RRM ELSE DO Reroute ON flows USING Switch'))

    # print(CoAs_Spec.parseString(if_s))
    # print(CoAs_Spec.parseString(elseif_s))
    # a = Optional(lparen) + ZeroOrMore(CoAs_Spec) + Optional(rparen)
    # print(a.parseString(
    #     '(IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% OUTCOME P && P <> ∅) THEN DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT '
    #     'ELSE IF (DO CheckElephantTCPFlow ON flows BY IDS-App USING rate  > 90% FOR DETECT OUTCOME E && E <> ∅) THEN DO Block ON flows OF E BY FIREWALL<1.5.6.4, admin> USING deny-command FOR PREVENT '
    #     'ELSE DO Replicate ON services OF (Reachable(L) && dport=80) USING replicate-command  '
    #     'ELSE DO Reroute ON flows USING Switch)'
    # ))

    TempContextExp = func_call
    ConfigContextExp = func_call
    DynamicContextExp = func_call
    Context_Exp = Group(TempContextExp | ConfigContextExp | DynamicContextExp).setName('exp')

    Rule = Optional(lparen) + Context_Exp + Optional(rparen) + Operator + OneOrMore(CoAs_Spec)
    # print(Rule.parseString(
    #     'Link-Flooded(T,L) -> IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% OUTCOME P && P <> ∅) THEN DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1> USING deny-command FOR PREVENT'))

    # parsed_policy = Rule.parseString(
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
    # with open('policy_1.txt') as f: # weired, it doesn't finde the file!
    with open('../policy/parser/policy_1.txt') as f:
        content = f.read()
        policy_string += content

    # print(policy_string)

    parsed_policy = Rule.parseString(policy_string)
    for rule in parsed_policy:
        print(rule)


if __name__ == '__main__':
    policy_parser()

"""
<Policy> ::= <Rule> | Policy> .<Rule>
<Operator> ::= OR | ; | ||
<weight> ::= 1…10
<Rule> ::=  [<weight>] (<Event_Exp>[, <Context_Exp>])   <CoAs_Spec> [UNTIL <Event_Exp>].
<Context_Exp> ::= <TempContextExp> | <ConfigContextExp> | <DynamicContextExp> 
<CoAs_Spec> ::= <CoAs>  | IF <CoA_Spec.OUTCOM=Value> 
            THEN <CoAs_Spec> ELSE  <CoAs_Spec>
<CoAs> ::= <Action_Spec> | <CoAs><Operator><CoAs>
<Action-spec> ::= [<Pre-condition>] DO <Action> ON <Objects> OF ObjAttributeValues 
                BY Actuator_Spec USING ActionAttribution FOR Goal OUTCOME Value [UNTIL <Event_Exp>]; 
ObjAttributeValues = Attributes <Op> Value | Attributes <Op> Value; ObjAttributeValues
Action ::= ConfigAction | InvestigationAction
ConfigAction ::= <FWActions> | <IDSActions>| <IPSecAction> | <ProxyAction> | 
        <MITRE-ATT&CK/CWE/CAPEC-MitigationActions> 
InvestigationAction ::= <SNMPGetAction> | <LogAuditAction> | <SplunkAction> | 
        <CameraActions> | <MITRE-ATT&CK/CWE/CAPEC-InvActions> |
<FW-Actions> ::= ACCEPT | DENY | REDIRECT | …
Object ::= Files | Flows | Links | Machines | .. 
Actuator_spec ::= <DevID, [type, loc, credentials, ..]>
ActionAttribution ::= <ENCRYPT, [KeySize, Alg, etc]>, ..

(Link-Flooded(T,L)) ->
     IF (DO CheckUDPICMPFlows ON flows BY IDS USING rate > 50% 
        OUTCOME P && P <> ∅) THEN	
            DO Block ON flows OF  (proto=CIMP or UDP in P) BY Switch<1.1.1.1>
            USING deny-command FOR PREVENT

    ELSE IF (DO CheckElephantTCPFlow ON flows BY IDS-App USING rate>90% 
            FOR DETECT OUTCOME E && E <> ∅) THEN	
                DO Block ON flows OF E BY FIREWALL<1.5.6.4, “admin”>
                USING deny-command FOR PREVENT

    ELSE IF (DO CheckNewComers ON flows BY IDS-App USING window < 1 
            OUTCOME N, rate && rate > 75%) THEN
                DO Rereoute ON flows OF (src_ip ∈ N) BY ROUTER USING RRM<>

    ELSE IF (DO CheckWhiteListed ON flows OF (src_ip ∈ WHITE-LIST) BY IDS-1 
        USING check-list-API  OUTCOME W && W <> ∅)  THEN
            DO Restrict ON flows OF src_ip ∉ W BY ROUTER USING BW-limit-command
"""
