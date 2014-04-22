from core.basescript import BaseScript

class HighClass(BaseScript):
    def __init__(self, id):
        BaseScript.__init__(self, id)
                  
high = HighClass("HIGH")    
