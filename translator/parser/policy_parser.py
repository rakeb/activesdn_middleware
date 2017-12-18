from anytree import RenderTree

from translator.lexer.policy_tokenizer import policy_lexer
from translator.parser.ActionSpecClass import ActionSpecClass
from translator.parser.EventClass import EventClass
from translator.parser.IfClass import IfClass
from translator.parser.TreeNode import TreeNode
from utilities import clips_list_checker

rule = None


def parse_nested_action_spec(root, list_body):
    left, operator, right = list_body[0], list_body[1], list_body[2]

    # operator
    op = TreeNode('op', parent=root)
    op.body = operator

    # left
    if clips_list_checker.is_clips_list_nested(left):
        parse_nested_action_spec(op, left)
    else:
        action_spec_node = ActionSpecClass('action_spec', parent=op)
        action_spec_node.body = left

    # right
    if clips_list_checker.is_clips_list_nested(right):
        parse_nested_action_spec(op, right)
    else:
        action_spec_node = ActionSpecClass('action_spec', parent=op)
        action_spec_node.body = right


def parse_coas_spec(root, list_body):
    # print(len(list_body))
    if clips_list_checker.is_action_spec(list_body):
        action_spec_node = ActionSpecClass('action_spec', parent=root)
        action_spec_node.body = list_body
    elif clips_list_checker.is_clips_list_nested(list_body):
        parse_nested_action_spec(root, list_body)
    elif clips_list_checker.is_if_then_else(list_body):
        if_c, if_body_c, then_c, then_body_c, else_c, else_body_c = clips_list_checker.decompose_if_then_else(list_body)
        if_node = IfClass('if_node', parent=root)
        if_node.body = if_body_c

        then_node = TreeNode('then_node', parent=root)
        # TODO need to check CoAs_Spec before consuming list
        then_node.body = then_body_c[0]
        parse_coas_spec(then_node, then_body_c[0])

        else_node = TreeNode('else_node', parent=root)
        # TODO again, the list consumtion is need to check
        if else_body_c[0] != 'IF':
            else_body_c = else_body_c[0]
        else_node.body = else_body_c
        parse_coas_spec(else_node, else_body_c)


def parse_tree(token_list):
    global rule
    # print(token_list)

    event = EventClass('event', parent=rule)
    event.body = token_list[0]

    op = TreeNode('op', parent=rule)
    op.body = token_list[1]

    coas_spec = TreeNode('coas_spec', parent=rule)
    coas_spec.body = token_list[2]

    parse_coas_spec(coas_spec, coas_spec.body)
    # parse_coas_spec(coas_spec, token_list[2])


def parser():
    global rule
    token_list = policy_lexer('../lexer/rule.txt')
    rule = TreeNode('rule')
    rule.body = token_list
    parse_tree(token_list)
    for pre, _, node in RenderTree(rule):
        treestr = u"%s%s" % (pre, node.name)
        print(treestr.ljust(8), node.name, node.body)
        # print(token_list)


if __name__ == '__main__':
    parser()
