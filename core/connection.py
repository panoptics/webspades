
import weakref
class BaseConnection():
    reactor  = None
    protocol = None
    server   = None
    connections = []

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
        self.connections.append(weakref.ref(client))
        for c in self.connections:
            if c is None:
                print "dead men dont tell tales"
                self.connections.remove(c)
        print self.connections
        print("onConnectCallback")

    def onDisConnectCallback(self, client):
        self.connections.remove( weakref.ref(client))
        del client
        print self.connections
        print("onDisConnectCallback")

class Connection(BaseConnection):
    def __init__(self, reactor, protocol, server):
        BaseConnection.__init__(self, reactor, protocol, server)

conn = Connection( reactor = None, protocol= None, server= None)