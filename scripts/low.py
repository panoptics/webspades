from core.basescript import BaseScript

class LowClass(BaseScript):
    value = 0

    def __init__(self):
        self.value =1
        BaseScript.__init__(self) 

    def fill(self, other):
        print "LOW yum"
        self.value= other.value +1

         
low = LowClass()   