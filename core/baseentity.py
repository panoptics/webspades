from simulation import sim
from vector3 import Vector3

class BaseEntity():
    id = None
    position = Vector3(0,0,0)
    orientation = Vector3(0,0,0)

    def __init__(self, id = None):
        self.id = id
        sim.registerEntity(self)
    def doTick(self):
        pass

class BaseScriptEntity(BaseEntity):
    reactor  = None
    protocol = None
    server   = None
    
    def __init__(self, id):
        sim.registerScriptEntity(self)
        BaseEntity.__init__(self, id)
