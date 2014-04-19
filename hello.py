import os
import gevent

from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
