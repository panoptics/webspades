import os
from twisted.web import static, server, resource
#from autobahn.twisted.choosereactor import install_reactor
from twisted.internet import task
from autobahn.twisted.websocket import WebSocketServerFactory,WebSocketServerProtocol
#reactor = install_reactor()
#print("Running on reactor {}".format(reactor))


class WebSpadesProtocol(WebSocketServerProtocol):
    isLeaf = True
    numberRequests = 0
    app = 0

    def onConnect(self, request):
	wsport= (os.environ.get('PORT', 8080))
        print("Client connect on port:"+str(wsport) )

    def onOpen(self):
        print("WebSocket connection open.")
        l = task.LoopingCall(self.runEverySecond)
        l.start(24.0) # call every second

    def onClose(self,reason,time,something):
        print("WebSocket connection closed.")
   
    def setServiceParent(application):
	self.app = application

    def runEverySecond(self):
        self.sendMessage(str("m" + str(self.numberRequests)), False)
        self.numberRequests+=1

    def onMessage(self, payload, isBinary):
        return 
        #self.numberRequests += 1
        ## just echo any WebSocket message received back to client
        ##
        #self.sendMessage(str("m" + str(self.numberRequests)), isBinary)

    def render_GET(self, request):
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.port) + "\n"

class WebSpadesServerFactory(WebSocketServerFactory):
    isLeaf = True
    render = True
    protocol = WebSpadesProtocol
    def render(self, request):
	return
