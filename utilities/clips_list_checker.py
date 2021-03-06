operators = ['OR', '&&', 'or', ';', '||', '->']


def is_clips_list_nested(i_list):
    if len(i_list) == 3 and i_list[1] in operators:
        return True
    return False


def is_action_spec(list_body):
    if list_body[0] == 'DO':
        return True
    return False


def is_list_multi_dimension(list_body):
    if len(list_body) == 1:
        if type(list_body[0]) == list:
            return True
    return False


def is_action_spec_followed_by_coas(list_body):
    if len(list_body) == 8:
        if list_body[0][0] == 'DO' and list_body[1] in operators and list_body[2] == 'IF':
            return True
    return False


def is_if_then_else(list_body):
    if len(list_body) == 6:
        if list_body[0] == 'IF':
            return True
    return False


def decompose_if_then_else(list_body):
    return list_body[0], list_body[1], list_body[2], list_body[3], list_body[4], list_body[5]


def decompose_action_spec_followed_by_coas(list_body):
    return list_body[0], list_body[1], list_body[2], list_body[3], list_body[4], list_body[5], list_body[6], \
           list_body[7]
