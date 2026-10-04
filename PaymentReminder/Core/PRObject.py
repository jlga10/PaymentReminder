from shiboken6 import Object

class PRObject(Object):
    @staticmethod
    def getName():
        return __name__