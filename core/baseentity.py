from simulation import sim
from vector3 import Vector3

class BaseEntity(object):
    id = None

    def __init__(self, id = None):
        self.id = id
        
    def doTick(self):
        pass

class BaseSimEntity(BaseEntity):
    id = None
    position = None
    orientation = None
    
    def __init__(self, id = None):
        self.id = id
        sim.registerEntity(self)
        self.position = self.getSpawnPos()
        self.orientation = self.getSpawnOrient()
        sim.registerScriptEntity(self)

    def getSpawnPos(self):
        return Vector3(0,0,0)

    def getSpawnOrient(self):
        return Vector3(0,0,0)

class BaseScriptEntity(BaseEntity):
    reactor  = None
    protocol = None
    server   = None

    def __init__(self, id):
        BaseEntity.__init__(self, id)
