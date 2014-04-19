import os
from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import protocol, reactor
from twisted.application import service, internet
from twisted.web import static, server, resource
from webspades import WebSpadesServerFactory
from twisted.internet.endpoints import serverFromString
from autobahn.twisted.choosereactor import install_reactor
from autobahn.twisted.websocket import WebSocketServerFactory, \
                                       WebSocketServerProtocol

from autobahn.twisted.resource import WebSocketResource, \
                                      HTTPChannelHixie76Aware

port= (os.environ.get('PORT', 8080))

def getWebService():
    #return internet.TCPServer(port, server.Site(HelloResource()) )
    #reactor = install_reactor()
    print("Running on reactor {}".format(reactor))
    #webSpadesService = service.MultiService()
    #fileServer = server.Site(WebSpadesServerFactory())
    #resource = WebSocketServerFactory("ws://localhost:" + str(port), False, False)
    #resource = WebSpadesServerFactory("ws://localhost:" + str(port))
    #root = File("./httdocs/")

    ## and our WebSocket server under "/ws"
    #root.putChild("ws", resource)

    ## both under one Twisted Web Site
    #site = Site(root)

    #return internet.TCPServer(port,site)
    #return internet.TCPServer(port,(WebSpadesServerFactory()))

    wsfactory = WebSpadesServerFactory()
    wsserver = serverFromString(reactor, "tcp:"+str(port))
    return wsserver.listen(wsfactory)
    #return webSpadesService

application = service.Application("webspades")

# attach the service to its parent application
service = getWebService()
#service.setServiceParent(application)
