
import weakref

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            print "found an existing instance"
        return cls._instances[cls]

def getListInstance(list, filter):
    for x in list:
        if filter(x):
            yield x

class BaseConnection():
    reactor  = None
    protocol = None
    server   = None
    connections = weakref.WeakValueDictionary()

    def __init__(self, reactor, protocol, server):
        self.reactor = reactor
        self.protocol = protocol
        self.server = server

    def setConnection(self, reactor, protocol, server):
        print "Connex set"
        self.reactor = reactor
        self.protocol = protocol
        self.server = server

    def CB(self, caller):
        print caller
        pass

    def onConnectCallback(self, client):

        if client.id in self.connections:
            del self.connections[client.id]

        self.connections[client.id] = client
        client.reactor = self.reactor
        client.protocol= self.protocol
        client.server = self.server
        print("onConnectCallback")

    def update(self):
        for c in self.connections:
            self.connections[c].doTick()

    def onDisConnectCallback(self, client):
        print "REMOVE CLIENT"
        del self.connections[client.id]
        print("onDisConnectCallback")

    def register(self, other):
        self.onConnectCallback(other)
        
class Connection(BaseConnection):
    def __init__(self, reactor, protocol, server):
        BaseConnection.__init__(self, reactor, protocol, server)

conn = Connection( reactor = None, protocol= None, server= None)

def Register(other):
    conn.register(other)
