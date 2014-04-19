import os
from twisted.web import static, server, resource
#from autobahn.twisted.choosereactor import install_reactor

from autobahn.twisted.websocket import WebSocketServerFactory,WebSocketServerProtocol
#reactor = install_reactor()
#print("Running on reactor {}".format(reactor))
port= (os.environ.get('PORT', 8080))

class WebSpadesProtocol(WebSocketServerProtocol):
    isLeaf = True
    numberRequests = 0
    app = 0
    def setServiceParent(application):
	self.app = application

    def onMessage(self, payload, isBinary):
        self.numberRequests += 1
        ## just echo any WebSocket message received back to client
        ##
        self.sendMessage(str(self.numberRequests), isBinary)

    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.numberRequests) + str(port) +  "\n"

class WebSpadesServerFactory(WebSocketServerFactory):
    protocol = WebSpadesProtocol
