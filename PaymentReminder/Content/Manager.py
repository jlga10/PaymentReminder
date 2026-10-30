class Manager:
    @staticmethod
    def getName():
        return __name__
        
    def __init__(self, name, email, telephone, alias):
        self.name = name
        self.email = email
        self.telephone = telephone
        self.alias = alias