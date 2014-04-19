import os

from twisted.internet import protocol, reactor
from twisted.application import service, internet
from twisted.web import static, server, resource
from webspades import WebSpadesServerFactory
from twisted.internet.endpoints import serverFromString
from autobahn.twisted.choosereactor import install_reactor
from autobahn.twisted.websocket import WebSocketClientFactory, \
                                       WebSocketClientProtocol

port= (os.environ.get('PORT', 8080))

def getWebService():
    #return internet.TCPServer(port, server.Site(HelloResource()) )
    #reactor = install_reactor()
    print("Running on reactor {}".format(reactor))
    webSpadesService = service.MultiService()
    fileServer = server.Site(static.File(os.getcwd()))

    internet.TCPServer(port, fileServer).setServiceParent(webSpadesService)

    wsfactory = WebSpadesServerFactory()
    wsserver = serverFromString(reactor, "tcp:"+str(8081))
    wsserver.listen(wsfactory)
    return webSpadesService

application = service.Application("webspades")

# attach the service to its parent application
service = getWebService()
service.setServiceParent(application)
