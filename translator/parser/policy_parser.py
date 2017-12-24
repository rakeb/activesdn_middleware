from anytree import RenderTree

from translator.lexer.policy_tokenizer import policy_lexer
from translator.parser.classes.ActionSpecClass import ActionSpecClass
from translator.parser.classes.EventClass import EventClass
from translator.parser.classes.IfClass import IfClass
from translator.parser.classes.TreeNode import TreeNode
from utilities import clips_list_checker

rule = None


def parse_nested_action_spec(root, list_body):
    left, operator, right = list_body[0], list_body[1], list_body[2]

    # operator
    op = TreeNode('op', parent=root)
    op.setBody(operator)

    # left
    if clips_list_checker.is_clips_list_nested(left):
        parse_nested_action_spec(op, left)
    else:
        action_spec_node = ActionSpecClass('action_spec', parent=op)
        action_spec_node.setBody(left)

    # right
    if clips_list_checker.is_clips_list_nested(right):
        parse_nested_action_spec(op, right)
    else:
        action_spec_node = ActionSpecClass('action_spec', parent=op)
        action_spec_node.setBody(right)


def parse_coas_spec(root, list_body):
    # we can also create a function to remove unnecessary multi dimension
    if clips_list_checker.is_list_multi_dimension(list_body):
        parse_coas_spec(root, list_body[0])
    # action spec
    if clips_list_checker.is_action_spec(list_body):
        action_spec_node = ActionSpecClass('action_spec', parent=root)
        action_spec_node.setBody(list_body)
    # multiple action spec
    elif clips_list_checker.is_clips_list_nested(list_body):
        parse_nested_action_spec(root, list_body)
    # if-then-else
    elif clips_list_checker.is_if_then_else(list_body):
        if_c, if_body_c, then_c, then_body_c, else_c, else_body_c = clips_list_checker.decompose_if_then_else(list_body)
        if_node = IfClass('if_node', parent=root)
        if_node.setBody(if_body_c)

        then_node = TreeNode('then_node', parent=root)
        # # TODO need to check CoAs_Spec before consuming list
        # then_node.setBody(then_body_c[0])
        # parse_coas_spec(then_node, then_body_c[0])

        then_node.setBody(then_body_c)
        parse_coas_spec(then_node, then_body_c)

        else_node = TreeNode('else_node', parent=root)
        # # TODO again, the list consumtion is need to check
        # if else_body_c[0] != 'IF':
        #     else_body_c = else_body_c[0]
        # else_node.setBody(else_body_c)
        # parse_coas_spec(else_node, else_body_c)
        else_node.setBody(else_body_c)
        parse_coas_spec(else_node, else_body_c)
    # action spec and then if then else
    elif clips_list_checker.is_action_spec_followed_by_coas(list_body):
        as_body_c, op_c, if_c, if_body_c, then_c, then_body_c, else_c, else_body_c = \
            clips_list_checker.decompose_action_spec_followed_by_coas(list_body)

        op = TreeNode('op', parent=root)
        op.setBody(op_c)

        action_spec_node = ActionSpecClass('action_spec', parent=op)
        action_spec_node.setBody(as_body_c)

        if_node = IfClass('if_node', parent=op)
        if_node.setBody(if_body_c)

        then_node = TreeNode('then_node', parent=op)
        # # TODO need to check CoAs_Spec before consuming list
        # then_node.setBody(then_body_c[0])
        # parse_coas_spec(then_node, then_body_c[0])
        then_node.setBody(then_body_c)
        parse_coas_spec(then_node, then_body_c)

        else_node = TreeNode('else_node', parent=op)
        # # TODO again, the list consumtion is need to check
        # if else_body_c[0][0] != 'DO':
        #     else_body_c = else_body_c[0]
        # else_node.setBody(else_body_c)
        # parse_coas_spec(else_node, else_body_c)
        else_node.setBody(else_body_c)
        parse_coas_spec(else_node, else_body_c)


def parse_tree(token_list):
    global rule
    # print(token_list)

    event = EventClass('event', parent=rule)
    event.setBody(token_list[0])

    op = TreeNode('op', parent=rule)
    op.setBody(token_list[1])

    coas_spec = TreeNode('coas_spec', parent=rule)
    coas_spec.setBody(token_list[2])

    parse_coas_spec(coas_spec, coas_spec.body)
    # parse_coas_spec(coas_spec, token_list[2])


def parser(filename='../lexer/rule.txt'):
    global rule
    token_list = policy_lexer(filename).asList()
    rule = TreeNode('rule')
    rule.body = token_list
    parse_tree(token_list)
    for pre, _, node in RenderTree(rule):
        treestr = u"%s%s" % (pre, node.name)
        print(treestr.ljust(8), node.body)
        # print(token_list)


if __name__ == '__main__':
    parser()
