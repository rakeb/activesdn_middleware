from translator.parser.classes.TreeNode import TreeNode


class IfClass(TreeNode):
    variable = None
    operator = None
    condition = None
    isUniary = False

    def parseBody(self):
        if len(self.body) == 1:
            self.isUniary = True
            self.condition = self.body[0]
        else:
            # self.isUniary = False
            self.variable = self.body[0]
            self.operator = self.body[1]
            self.condition = self.body[2]

    def setBody(self, body):
        self.body = body
        self.parseBody()

    def __str__(self):
        print("IfClass")
