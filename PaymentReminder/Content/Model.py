from . import Brand as brand
from . import Talent as talent
from . import Manager as manager
from . import Collaboration as collaboration

class Model(object):
    def __init__(self):
        self.talents = dict()
        self.managers = dict()
        self.brands = dict()
        self.collaborations = dict()
    
#region Brand CRUD
    def createBrand(self, brand_name, email, telephone):
        if brand_name in self.brands:
            print(f"Brand '{brand_name}' already exists.")
            return False
        else:
            print(f"Creating brand '{brand_name}' with email '{email}' and telephone '{telephone}'.")
            new_brand = brand.Brand(brand_name, email, telephone)
            self.brands[brand_name] = new_brand
            return True

    def editBrand(self, brand_name, new_name=None, new_email=None, new_telephone=None):
        if brand_name in self.brands:
            brand_to_edit = self.brands[brand_name]
            if new_name:
                brand_to_edit.name = new_name
            if new_email:
                brand_to_edit.email = new_email
            if new_telephone:
                brand_to_edit.telephone = new_telephone
            print(f"Brand '{brand_name}' updated to: {brand_to_edit}")
            return True
        else:
            print(f"Brand '{brand_name}' does not exist.")
            return False

    def deleteBrand(self, brand_name):
        if brand_name in self.brands:
            del self.brands[brand_name]
            print(f"Brand '{brand_name}' deleted.")
            return True
        else:
            print(f"Brand '{brand_name}' does not exist.")
            return False

    def getBrand(self, brand_name):
        return self.brands.get(brand_name, None)
#endregion Brand CRUD
#region Talent CRUD
    def createTalent(self, talent_name, email, telephone, alias=None):
        if talent_name in self.talents:
            print(f"Talent '{talent_name}' already exists.")
            return False
        else:
            print(f"Creating talent '{talent_name}' with email '{email}' and telephone '{telephone}', alias '{alias}'.")
            new_talent = talent.Talent(talent_name, email, telephone, alias=None)
            self.talents[talent_name] = new_talent
            return True

    def editTalent(self, talent_name, new_name=None, new_email=None, new_telephone=None, new_alias=None):
        if talent_name in self.talents:
            talent_to_edit = self.talents[talent_name]
            if new_name:
                talent_to_edit.name = new_name
            if new_email:
                talent_to_edit.email = new_email
            if new_telephone:
                talent_to_edit.telephone = new_telephone
            if new_alias:
                talent_to_edit.alias = new_alias
            print(f"Talent '{talent_name}' updated to: {talent_to_edit}")
            return True
        else:
            print(f"Talent '{talent_name}' does not exist.")
            return False

    def deleteTalent(self, talent_name):
        if talent_name in self.talents:
            del self.talents[talent_name]
            print(f"Talent '{talent_name}' deleted.")
            return True
        else:
            print(f"Talent '{talent_name}' does not exist.")
            return False

    def getTalent(self, talent_name):
        return self.talents.get(talent_name, None)
#endregion Talent CRUD
#region Manager CRUD
    def createManager(self, manager_name, email, telephone, alias):
        if manager_name in self.managers:
            print(f"Manager '{manager_name}' already exists.")
            return False
        else:
            print(f"Creating manager '{manager_name}' with email '{email}' and telephone '{telephone}', alias '{alias}'.")
            new_manager = manager.Manager(manager_name, email, telephone, alias)
            self.managers[manager_name] = new_manager
            return True
        
    def editManager(self, manager_name, new_name=None, new_email=None, new_telephone=None, new_alias=None):
        if manager_name in self.managers:
            manager_to_edit = self.managers[manager_name]
            if new_name:
                manager_to_edit.name = new_name
            if new_email:
                manager_to_edit.email = new_email
            if new_telephone:
                manager_to_edit.telephone = new_telephone
            if new_alias:
                manager_to_edit.alias = new_alias
            print(f"Manager '{manager_name}' updated to: {manager_to_edit}")
            return True
        else:
            print(f"Manager '{manager_name}' does not exist.")
            return False

    def deleteManager(self, manager_name):
        if manager_name in self.managers:
            del self.managers[manager_name]
            print(f"Manager '{manager_name}' deleted.")
            return True
        else:
            print(f"Manager '{manager_name}' does not exist.")
            return False

    def getManager(self, manager_name):
        return self.managers.get(manager_name, None)
#endregion Manager CRUD
#region Collaboration CRUD
    def createCollaboration(self, collaboration_name, brand_name, talent_name):
        if collaboration_name in self.collaborations:
            print(f"Collaboration '{collaboration_name}' already exists.")
            return False
        else:
            print(f"Creating collaboration '{collaboration_name}' between brand '{brand_name}' and talent '{talent_name}'.")
            new_collaboration = collaboration.Collaboration(collaboration_name, brand_name, talent_name)
            self.collaborations[collaboration_name] = new_collaboration
            return True

    def editCollaboration(self, collaboration_name, new_name=None, new_brand_name=None, new_talent_name=None):
        if collaboration_name in self.collaborations:
            collaboration_to_edit = self.collaborations[collaboration_name]
            if new_name:
                collaboration_to_edit.name = new_name
            if new_brand_name:
                collaboration_to_edit.brand_name = new_brand_name
            if new_talent_name:
                collaboration_to_edit.talent_name = new_talent_name
            print(f"Collaboration '{collaboration_name}' updated to: {collaboration_to_edit}")
            return True
        else:
            print(f"Collaboration '{collaboration_name}' does not exist.")
            return False

    def deleteCollaboration(self, collaboration_name):
        if collaboration_name in self.collaborations:
            del self.collaborations[collaboration_name]
            print(f"Collaboration '{collaboration_name}' deleted.")
            return True
        else:
            print(f"Collaboration '{collaboration_name}' does not exist.")
            return False

    def getCollaboration(self, collaboration_name):
        return self.collaborations.get(collaboration_name, None)
#endregion Collaboration CRUD