class Talent:
    @staticmethod
    def getName():
        return __name__

    def __init__(self, name, email, alias):
        self.name = name
        self.email = email
        self.alias = alias