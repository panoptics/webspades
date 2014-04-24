
import weakref

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
        #for c in self.connections:
        #   self.connections[c].doTick()
        pass

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
