from core.basescript import BaseScript

class LowClass(BaseScript):
    def __init__(self, id):
        BaseScript.__init__(self, id)
             
low = LowClass("LOWCLASS")    