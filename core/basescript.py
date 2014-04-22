
from core.connection import Register

class BaseScript():
    def __init__(self):
        Register(self)
        print self.__class__