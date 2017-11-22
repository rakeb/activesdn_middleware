from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

pStack = Stack()
eTree = BinaryTree('')
pStack.push(eTree)
currentTree = eTree
operators = ['OR', 'or', ';', '||']

a_list = [
    [
        [
            'DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY',
            ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT',
            'OUTCOME',
            'O1'
        ],
        '||',
        [
            'DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY',
            ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR',
            'PREVENT', 'OUTCOME', 'O2'
        ]
    ],
    ';',
    [
        [
            'DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY',
            ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR', 'PREVENT',
            'OUTCOME',
            'O3'
        ],
        '||',
        [
            'DO', 'Block', 'ON', 'flows', 'OF', ['proto', '=', 'CIMP', 'or', 'UDP', 'in', 'P'], 'BY',
            ['Switch', '<', ['1', '.', '1', '.', '1', '.', '1'], '>'], 'USING', 'deny-command', 'FOR',
            'PREVENT', 'OUTCOME', 'O4'
        ]
    ]
]


# def buildParseTree(fpexp):
#     fplist = fpexp.split()
#     pStack = Stack()
#     eTree = BinaryTree('')
#     pStack.push(eTree)
#     currentTree = eTree
#     for i in fplist:
#         if i == '(':
#             currentTree.insertLeft('')
#             pStack.push(currentTree)
#             currentTree = currentTree.getLeftChild()
#         elif i not in ['+', '-', '*', '/', ')']:
#             currentTree.setRootVal(int(i))
#             parent = pStack.pop()
#             currentTree = parent
#         elif i in ['+', '-', '*', '/']:
#             currentTree.setRootVal(i)
#             currentTree.insertRight('')
#             pStack.push(currentTree)
#             currentTree = currentTree.getRightChild()
#         elif i == ')':
#             currentTree = pStack.pop()
#         else:
#             raise ValueError
#     return eTree


def is_nested_list(i_list):
    if type(i_list) is list:
        if len(i_list) > 1:
            return True
    return False


def is_nested_updated(i_list):
    if len(i_list) == 3 and i_list[1] in operators:
        return True
    return False


def is_nested(i_list):
    if len(i_list) > 1:
        for item in i_list:
            if len(item) > 1:
                for i in item:
                    if i in operators:
                        return True
    return False


def build_parse_tree(clips_list, root):
    left, operator, right = clips_list[0], clips_list[1], clips_list[2]
    # left
    root.insertLeft('')
    if is_nested_updated(left):
        build_parse_tree(left, root.getLeftChild())
    else:
        root.getLeftChild().setRootVal(left)

    # operator
    root.setRootVal(operator)

    # right
    root.insertRight('')
    if is_nested_updated(right):
        build_parse_tree(right, root.getRightChild())
    else:
        root.getRightChild().setRootVal(right)


def list_to_postfix_updated(input_list):
    global pStack
    global eTree
    global currentTree

    # zzz = [[['a','||','b'],'or', ['c','||','d']], ';' , ['e','||','f']]
    # list has multiple values
    if is_nested(input_list):

        head, tail = input_list[0], input_list[1:]

        if head not in operators:
            # create new node
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
            list_to_postfix(head)
        else:
            # while currentTree.getRootVal() == '' and not pStack.isEmpty():
            currentTree = pStack.pop()
            currentTree.setRootVal(head)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
            tail = tail[0]

        # print(head)
        # print(tail)
        # list_to_postfix(head)
        list_to_postfix(tail)
        # currentTree = pStack.pop()
    else:
        for i in input_list:
            if i not in operators:
                if input_list.index(i) == 0:
                    currentTree.insertLeft('')
                    pStack.push(currentTree)
                    currentTree = currentTree.getLeftChild()
                currentTree.setRootVal(i)
                parent = pStack.pop()
                currentTree = parent
            elif i in operators:
                currentTree.setRootVal(i)
                currentTree.insertRight('')
                pStack.push(currentTree)
                currentTree = currentTree.getRightChild()
                # currentTree = pStack.pop()
                # eTree.postorder()


def list_to_postfix(input_list):
    global pStack
    global eTree
    global currentTree

    # zzz = [[['a','||','b'],'or', ['c','||','d']], ';' , ['e','||','f']]
    # list has multiple values
    if is_nested(input_list):

        head, tail = input_list[0], input_list[1:]

        if head not in operators:
            # create new node
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
            list_to_postfix(head)
        else:
            # while currentTree.getRootVal() == '' and not pStack.isEmpty():
            #     currentTree = pStack.pop()
            currentTree.setRootVal(head)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
            tail = tail[0]

        # print(head)
        # print(tail)
        # list_to_postfix(head)
        list_to_postfix(tail)
        currentTree = pStack.pop()
    else:
        for i in input_list:
            if i not in operators:
                if input_list.index(i) == 0:
                    currentTree.insertLeft('')
                    pStack.push(currentTree)
                    currentTree = currentTree.getLeftChild()
                currentTree.setRootVal(i)
                parent = pStack.pop()
                currentTree = parent
            elif i in operators:
                currentTree.setRootVal(i)
                currentTree.insertRight('')
                pStack.push(currentTree)
                currentTree = currentTree.getRightChild()
                # currentTree = pStack.pop()
                # eTree.postorder()


if __name__ == '__main__':
    # input_list = [
    #     [
    #         ['a'],
    #         '||',
    #         ['b']
    #     ],
    #     ';',
    #     ['c']
    # ]
    #
    input_list = [
        ['a'],
        '||',
        ['b']
    ]

    input_list = [
        [
            ['a'],
            '||',
            ['b']
        ],
        'or',
        ['c']
    ]

    input_list = [
        [
            [
                ['a'],
                '||',
                ['b']
            ],
            'or',
            [
                ['c'],
                '||',
                ['d']
            ],
        ],
        ';',
        [
            ['e'],
            '||',
            ['f']
        ],
    ]

    # list1 = ['1', '2', '3']
    # str1 = ''.join(list1)
    # print(str1)

    # list_to_postfix_updated(input_list)
    # list_to_postfix(a_list)
    # eTree.postorder()
    # print(is_nested_list([1, 2, 3]))
    build_parse_tree(a_list, currentTree)
    # build_parse_tree(input_list, currentTree)
    eTree.postorder()
