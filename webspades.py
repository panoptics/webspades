import os, time
from twisted.web import static, server, resource
#from autobahn.twisted.choosereactor import install_reactor
from twisted.internet import task

from autobahn.twisted.websocket import WebSocketServerFactory,WebSocketServerProtocol
#reactor = install_reactor()
#print("Running on reactor {}".format(reactor))
from codecs import (utf_8_encode, utf_8_decode, latin_1_encode, latin_1_decode)


import collections

class Message():
    payload = None
    timestamp =0
    def __init__(self, payload, timestamp ):
        self.payload = payload
        self.timestamp = timestamp

class WebSpadesProtocol(WebSocketServerProtocol):
    numberRequests = 0
    lastping =0
    reactor = None
    pingtime = 0
    messages = collections.deque()

    def onConnect(self, request):
        wsport= (os.environ.get('PORT', 8080))
        print("Client connect on port:"+str(wsport) )

    def onOpen(self):
        print("WebSocket connection open.")
        l = task.LoopingCall(self.runEverySecond)
        l.start(5.0)

    def onClose(self,reason,time,something):
        print("WebSocket connection closed. : " + str(len(self.messages)))


    def onPong(self, pong):
        self.pingtime = self.lastping-self.reactor.seconds()
        print( "pingtime:" + str(self.pingtime)) 

    def runEverySecond(self):
        self.lastping = self.reactor.seconds()
        self.sendPing()
        tosend = utf_8_encode(unicode(
            str(self.pingtime), 'latin-1'))[0]      

        self.sendMessage(str(self.pingtime), True)
        self.numberRequests+=1

    def onMessage(self, payload, isBinary):
        self.messages.append( Message(payload, self.reactor.seconds()) )

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
    protocol = WebSpadesProtocol
    def render(self, request):
	    return
