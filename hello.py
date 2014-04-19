import sys
import os
"""import gevent"""

PO  = os.environ['PORT']
port = int(sys.argv[-1])

from twisted.internet import reactor
from twisted.web import server, resource
from twisted.web.server import Site, NOT_DONE_YET
from twisted.internet.threads import deferToThread

class HelloResource(resource.Resource):
    isLeaf = True
    numberRequests = 0
    
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.numberRequests) + "\n"

reactor.listenTCP(port, server.Site(HelloResource()))
reactor.run()
