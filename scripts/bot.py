
from core.basescript import BaseScript
from core.baseentity import BaseScriptEntity

class BottomClass(BaseScript, BaseScriptEntity):

    # __metaclass__ = Singleton
    def __init__(self, id):
        BaseScript.__init__(self, id)
        BaseScriptEntity.__init__(self, id)

    def doTick(self):
        self.position.x+=1
        print self.position
        BaseScript.doTick(self)
   
bot = BottomClass("BOTTOM1")             
 