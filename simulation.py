
""" sim runs independantly of network """


import os, time, math, weakref

from twisted.internet import task
from autobahn.twisted.choosereactor import install_reactor
from sets import Set




class BaseSimulation():
    reactor  = None
    protocol = None
    server   = None
    paused   = True
    conn     = None
    loop     = None
    freq     = 0.0
    pertick  = 10 
    simulants= Set()
    entities = weakref.WeakValueDictionary()

    def __init__(self, reactor, protocol, server, conn, freq = 0.2 ):
        self.reactor = reactor
        self.protocol = protocol
        self.server = server
        self.tticks =0
        self.freq = freq
        self.conn = conn

    def op(self, sctime =0.0):
        print( self.reactor.seconds())
        self.conn.update()
        for c in self.entities:
            self.entities[c].doTick()

    def tick(self):
        inter = self.freq/float(self.pertick)
        ntime = math.floor(self.reactor.seconds())
        now = self.reactor.seconds()
        for x in range(1,self.pertick+1):
            self.reactor.callLater(ntime-now+(float(x)*inter), self.op)
        self.tticks+=1

    def enactSim(self):
        self.loop = task.LoopingCall(self.tick)
        """ wait for next sim tick to start sim"""
        self.loop.start(self.freq, now = False)

    def start(self):
        """ Start the looping call ON the next second 
        (at least as close as possible)"""
        if self.loop == None:
            ntime = math.floor(self.reactor.seconds())
            self.reactor.callLater(ntime-self.reactor.seconds()+1.0, self.enactSim )
    
    def registerEntity(self, other):
        if other.id in self.entities:
            del self.entities[other.id]
        self.entities[other.id] = other

    def registerScriptEntity(self, other):
        other.reactor = self.reactor
        other.protocol= self.protocol
        other.server  = self.server

    def stop(self):
    	self.loop.stop()
        return

    def pause(self):
        return

    def getTicks(self):
        return self.ticks


class Simulation(BaseSimulation):
    protocol = None
    server   = None
    paused   = True

    def __init__(self, reactor, protocol, server, conn, freq = 0.2 ):
        BaseSimulation.__init__(self, reactor, protocol, server, conn, freq)

sim = Simulation( reactor = None, protocol= None, server= None, conn = None)
