from core.basescript import BaseScript

class HighClass(BaseScript):
    value = 0

    def __init__(self):
        self.value =1
        BaseScript.__init__(self) 

    def fill(self, other):
        print "High yum"
        self.value= other.value +1
         
high = HighClass() 