class ObjectAttributesValues:
    key = None
    operator = None
    value = None
    body = None

    def __init__(self, body):
        self.body = body
        self.parseBody()

    def parseBody(self):
        self.key = self.body[0]
        self.operator = self.body[1]
        self.value = self.body[2:len(self.body) - 1]


class ActuatorSpec:
    deviceName = None
    type = None
    location = None
    credentials = None
    body = None

    def __init__(self, body):
        self.body = body
        self.parseBody()

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


class ActionAttribution:
    variable = None
    operator = None
    condition = None
    isUniary = False

    def __init__(self, body):
        self.body = body
        self.parseBody()

    def parseBody(self):
        if type(self.body) == list:
            # self.isUniary = False
            self.variable = self.body[0]
            self.operator = self.body[1]
            self.condition = self.body[2]
        else:
            self.isUniary = True
            self.condition = self.body[0]