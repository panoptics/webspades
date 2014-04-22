
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



    def onConnectCallback(self, client):
        for i in getListInstance(self.connections, lambda x: isinstance(x, client.__class__ )):
            client.fill(i)

        if str(client.__class__) in self.connections:
            client.fill(self.connections[str(client.__class__)])
            del self.connections[str(client.__class__)] 
        self.connections[str(client.__class__)] = client
        print client.value
        print self.connections
        print("onConnectCallback")

    def onDisConnectCallback(self, client):
        self.connections.remove((client))
        del client
        print self.connections
        print("onDisConnectCallback")

    def register(other):
        conn.onConnectCallback(other)
class Connection(BaseConnection):
    def __init__(self, reactor, protocol, server):
        BaseConnection.__init__(self, reactor, protocol, server)

conn = Connection( reactor = None, protocol= None, server= None)

def Register(other):
    conn.onConnectCallback(other)
