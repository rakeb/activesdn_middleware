from translator.parser.classes.TreeNode import TreeNode


class EventClass(TreeNode):
    eventName = None
    paramList = None

    def parseBody(self):
        self.eventName = self.body[0]
        self.paramList = self.body[self.body.index('(') + 1:self.body.index(')')]

    def setBody(self, body):
        self.body = body
        self.parseBody()

    def __str__(self):
        print("EventClass")
