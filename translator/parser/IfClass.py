from translator.parser.TreeNode import TreeNode


class IfClass(TreeNode):
    def setBody(self, body):
        self.body = body

    def __str__(self):
        print("IfClass")
