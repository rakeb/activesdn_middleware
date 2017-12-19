from anytree import NodeMixin


class TreeNode(NodeMixin):
    name = None
    body = None

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def parseBody(self):
        pass

    def setBody(self, body):
        self.body = body
        self.parseBody()

    def getName(self):
        return self.name

    def __str__(self):
        print("Node")
