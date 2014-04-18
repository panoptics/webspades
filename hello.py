import os
from twisted.web import server, resource
from twisted.internet import reactor
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
