from translator.parser.classes.TreeNode import TreeNode


class ActionSpecClass(TreeNode):
    def parseBody(self):
        pass

    def setBody(self, body):
        self.body = body
        self.parseBody()

    def __str__(self):
        print("ActionSpecClass")
