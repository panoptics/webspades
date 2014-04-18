import os
from twisted.web import server, resource
from twisted.internet import reactor
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'





class HelloResource(resource.Resource):
    isLeaf = True
    numberRequests = 0
    
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.numberRequests) + "\n"

reactor.listenTCP(82, server.Site(HelloResource()))
reactor.run()

