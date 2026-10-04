class Brand:
    @staticmethod
    def getName():
            return __name__
    
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone