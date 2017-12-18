from translator.parser.TreeNode import TreeNode


class EventClass(TreeNode):
    def setBody(self, body):
        self.body = body

    def __str__(self):
        print("EventClass")
