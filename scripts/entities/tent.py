from core.baseentity import BaseSimEntity
from vector3 import Vector3
class TentEntity(BaseSimEntity):

    # __metaclass__ = Singleton
    def __init__(self, id):
        BaseSimEntity.__init__(self, id)

    def getSpawnPos(self):
        return Vector3(100,0,0)

    def doTick(self):
        self.position.x+=.12
        if hasattr(self,"position"):
            print self.position
        BaseSimEntity.doTick(self)

tent = TentEntity("TentEntity")            
     