import os
port = os.environ['PORT']

from flask import Flask
from twisted.web import server, resource
from twisted.internet import reactor

app = Flask(__name__)


class HelloResource(resource.Resource):
    isLeaf = True
    numberRequests = 0
    
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.numberRequests) + "\n"


from twisted.internet import reactor
reactor.listenTCP(port, server.Site(HelloResource()))
reactor.run()
