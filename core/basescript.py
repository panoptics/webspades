
from core.connection import Register

class BaseScript():
    id = None
    value =0
    reactor  = None
    protocol = None
    server   = None

    def __init__(self, id):
        self.value =1
        self.id = id
        Register(self)

    def doTick(self):
        pass
    def __del__(self):
        print "DEREWARARWR"
    def fill(self, other):
        print "mid yum"
        self.value= other.value +1