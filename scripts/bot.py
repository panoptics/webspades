
from core.basescript import BaseScript

class BottomClass(BaseScript):
    value = 0
    # __metaclass__ = Singleton
    def __init__(self):
        self.value =1
        BaseScript.__init__(self)

    def fill(self, other):
        print "mid yum"
        self.value= other.value +1

bot = BottomClass()            
