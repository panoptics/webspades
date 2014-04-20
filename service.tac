""" sim runs independantly of network """


import ctypes, os, time

from twisted.web import server, resource
from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import protocol, reactor, task
from twisted.application import service, internet
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile

from autobahn.twisted.choosereactor import install_reactor
from autobahn.twisted.websocket import WebSocketServerFactory, \
                                       WebSocketServerProtocol
from autobahn.twisted.resource import WebSocketResource
from webspades import WebSpadesServerFactory,WebSpadesProtocol
from simulation import Simulation

port= (os.environ.get('PORT', 8080))


def getWebService():
    #reactor = install_reactor()
    #print("Running on reactor {}".format(reactor))

    factory1 = WebSpadesServerFactory("ws://localhost:" + str(port),
                                     debug = False,
                                     debugCodePaths = False)

    resource1 = WebSocketResource(factory1)
    

    root = File("./htdocs/")
    root.putChild("ws", resource1)
    site = Site(root)
    server = reactor.listenTCP(port, site)
    #reactor.seconds = perf_counter
    factory1.protocol.reactor = reactor
    #sim = Simulation(reactor, factory1.protocol, server)
    #sim.start(1.0)
    return server

application = service.Application("webspades")

#logfile = DailyLogFile("webspades.log", "/tmp")
#application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

# attach the service to its parent application
service = getWebService()
#service.setServiceParent(application)
