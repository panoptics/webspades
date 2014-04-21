
""" sim runs independantly of network """


import os, time, math

from twisted.internet import task
from autobahn.twisted.choosereactor import install_reactor
from sets import Set

class BaseSimulation():
    reactor  = None
    protocol = None
    server   = None
    paused   = True
    loop     = None
    freq     = 0.0
    pertick  = 4 
    simulants= Set()

    def __init__(self, reactor, protocol, server, freq = 0.2 ):
        self.reactor = reactor
        self.protocol = protocol
        self.server = server
        self.tticks =0
        self.freq = freq

    def op(self, sctime =0.0):
        print( self.reactor.seconds())
        return

    def tick(self):
        inter = 1.0/float(self.pertick)
        ntime = math.floor(self.reactor.seconds())
        for x in range(1,self.pertick+1):
            self.reactor.callLater(ntime-self.reactor.seconds()+(float(x)*inter), self.op)

        self.tticks+=1
        

    def enactSim(self):
        self.loop = task.LoopingCall(self.tick)
        """ wait for next sim tick to start sim"""
        self.loop.start(self.freq, now = False)

    def start(self, freq ):
        self.freq = freq
        """ Start the looping call ON the next second 
        (at least as close as possible)"""
        if self.loop == None:
            ntime = math.floor(self.reactor.seconds())
            self.reactor.callLater(ntime-self.reactor.seconds()+1.0, self.enactSim )


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

    def __init__(self, reactor, protocol, server, freq = 0.2 ):
        BaseSimulation.__init__(self, reactor, protocol, server, freq)
