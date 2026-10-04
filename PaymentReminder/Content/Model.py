from . import Brand as brand


class Model(object):
    def __init__(self):
        self.talents = dict()
        self.managers = dict()
        self.brands = dict()
        self.collaborations = dict()

    def createBrand(self, brand_name, email, telephone):
        if brand_name in self.brands:
            print(f"Brand '{brand_name}' already exists.")
            return False
        else:
            print(f"Creating brand '{brand_name}' with email '{email}' and telephone '{telephone}'.")
            new_brand = brand.Brand(brand_name, email, telephone)
            self.brands[brand_name] = new_brand
            return True