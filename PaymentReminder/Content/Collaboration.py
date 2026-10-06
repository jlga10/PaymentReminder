class Collaboration:
    @staticmethod
    def getName():
            return __name__
    
    def __init__(self, id, talent, brand, manager, total_amount, billing_date, remaining_days, charged):
        self.id = id
        self.talent = talent
        self.brand = brand
        self.manager = manager
        self.total_amount = total_amount
        self.billing_date = billing_date
        self.remaining_days = remaining_days
        self.charged = charged