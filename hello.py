import os
import logging
import gevent
from flask import Flask, render_template
from flask_sockets import Sockets


app = Flask(__name__)
app.debug = 'DEBUG' in os.environ

from twisted.internet import reactor

def aSillyBlockingMethod(x):
    import time
    time.sleep(2)
    print x

@app.route('/')
def index():
# run method in thread
    reactor.callInThread(aSillyBlockingMethod, "2 seconds have passed")
    reactor.run()
    return "hi"
