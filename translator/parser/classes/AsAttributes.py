class ObjectAttributesValues:
    key = None
    operator = None
    value = None
    body = None
    pFact = None

    def __init__(self, body):
        self.body = body
        self.parseBody()
        self.prologFact()

    def parseBody(self):
        self.key = self.body[0]
        self.operator = self.body[1]
        self.value = self.body[2:len(self.body)]

    def prologFact(self):
        self.pFact = "%s, %s" % (self.key, self.value)
        # print("fact: ", self.pFact)
        #TODO
        self.pFact = self.pFact.lower()
        return self.pFact


class ActuatorSpec:
    deviceName = None
    # type = None
    location = None
    credentials = None
    body = None
    pFact = None

    def __init__(self, body):
        self.body = body
        self.parseBody()
        self.prologFact()

    def parseBody(self):
        if type(self.body) == list:
            self.deviceName = self.body[0]
            if len(self.body) > 1:
                body = self.body[self.body.index('<') + 1:self.body.index('>')]
                self.location = body[0]
                if len(body) > 1:
                    self.credentials = body[1:]
        else:
            self.deviceName = self.body

    def prologFact(self):
        if self.deviceName is not None:
            self.pFact = "%s" % self.deviceName
        if self.location is not None:
            self.pFact += ", %s" % self.location
        if self.credentials is not None:
            self.pFact += ", %s" % self.credentials
        # TODO
        self.pFact = self.pFact.lower()
        # print("ActuatorSpec fact: ", self.pFact)
        return self.pFact


class ActionAttribution:
    variable = None
    operator = None
    condition = None
    isUniary = False
    pFact = None

    def __init__(self, body):
        self.body = body
        self.parseBody()
        self.prologFact()

    def parseBody(self):
        if type(self.body) == list:
            # self.isUniary = False
            self.variable = self.body[0]
            self.operator = self.body[1]
            self.condition = self.body[2]
        else:
            self.isUniary = True
            self.variable = self.body

    def prologFact(self):
        if self.variable is not None:
            self.pFact = "%s" % self.variable
        if self.operator is not None:
            self.pFact += ", %s" % self.operator
        if self.condition is not None:
            self.pFact += ", %s" % self.condition
        # TODO make lower here?
        self.pFact = self.pFact.lower()
        # print("ActionAttribution fact: ", self.pFact)
        # return self.pFact
        return self.body
