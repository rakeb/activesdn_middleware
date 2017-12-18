from anytree import NodeMixin


class TreeNode(NodeMixin):
    name = None
    body = None

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent


    def getName(self):
        return self.name

    def __str__(self):
        print("Node")
