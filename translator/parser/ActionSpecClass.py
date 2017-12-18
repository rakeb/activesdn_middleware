from translator.parser.TreeNode import TreeNode


class ActionSpecClass(TreeNode):
    # body = None
    #
    def setBody(self, body):
        self.body = body

    def __str__(self):
        print("ActionSpecClass")
