import itertools

from translator.parser.classes.AsAttributes import ObjectAttributesValues, ActuatorSpec, ActionAttribution
from translator.parser.classes.TreeNode import TreeNode


class ActionSpecClass(TreeNode):
    doAttribute = None  # str
    onAttribute = None  # str
    ofAttribute = None
    byAttribute = None
    usingAttribute = None
    forAttribute = None
    outcomeAttribute = None
    untilAttribute = None
    newId = itertools.count()
    pFact = None

    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.id = "as_id_" + str(next(self.newId))
        # print("Name: %s, ID %d" %(name, self.id))

    def parseBody(self):
        # set DO
        do_atr_index = self.body.index('DO') + 1
        self.doAttribute = self.body[do_atr_index]

        # set ON
        on_atr_index = self.body.index('ON') + 1
        self.onAttribute = self.body[on_atr_index]

        # set OF
        of_atr_index = self.body.index('OF') + 1
        self.ofAttribute = ObjectAttributesValues(self.body[of_atr_index])

        # set BY
        by_atr_index = self.body.index('BY') + 1
        self.byAttribute = ActuatorSpec(self.body[by_atr_index])

        # set USING
        using_atr_index = self.body.index('USING') + 1
        self.usingAttribute = ActionAttribution(self.body[using_atr_index])

        # set FOR
        for_atr_index = self.body.index('FOR') + 1
        self.forAttribute = self.body[for_atr_index]

        # set FOR
        for_atr_index = self.body.index('FOR') + 1
        self.forAttribute = self.body[for_atr_index]

        # set OUTCOME
        outcome_atr_index = self.body.index('OUTCOME') + 1
        self.outcomeAttribute = self.body[outcome_atr_index]

    def prologFact(self):
        #                          id,do, on, of, by, using,for, outcome
        self.pFact = 'action_spec(%s, %s, %s, %s, %s, %s, %s, %s).' % (
        self.id, self.doAttribute, self.onAttribute, self.ofAttribute.prologFact(), self.byAttribute.prologFact(),
        self.usingAttribute.prologFact(), self.forAttribute, self.outcomeAttribute)

        self.pFact = self.pFact.lower()

        #f = open("prolog.pl", "a")
        #f.write(self.pFact)
        #f.write("\n")
        #f.close()

        # print("AS : ", self.pFact)

    def setBody(self, body):
        self.body = body
        self.parseBody()
        self.prologFact()

    def __str__(self):
        print("ActionSpecClass")
