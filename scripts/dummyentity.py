from core.baseentity import BaseScriptEntity

class DummyEntity(BaseScriptEntity):

    # __metaclass__ = Singleton
    def __init__(self, id):
        BaseScriptEntity.__init__(self, id)

    def doTick(self):
        print(self.id)
        BaseScriptEntity.doTick(self)
   
dum = DummyEntity("DummyEntity")            
    