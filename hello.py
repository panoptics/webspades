import os
import gevent

PO  = os.environ['PORT']

from twisted.web import server, resource
from twisted.internet import reactor

class HelloResource(resource.Resource):
    isLeaf = True
    numberRequests = 0
    
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.numberRequests) + "\n"

reactor.listenTCP(PO, server.Site(HelloResource()))
reactor.run()
