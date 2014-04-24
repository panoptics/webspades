#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time
from twisted.web import static, server, resource
#from autobahn.twisted.choosereactor import install_reactor
from twisted.internet import task

from autobahn.twisted.websocket import WebSocketServerFactory,WebSocketServerProtocol
#reactor = install_reactor()
#print("Running on reactor {}".format(reactor))
from codecs import (utf_8_encode, utf_8_decode, latin_1_encode, latin_1_decode)
import urllib

import collections
import json
import hashlib

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
    onConnectCallback = None
    onDisConnectCallback = None
    pingtime = 0
    messages = collections.deque()
    connex   = 0
    client_id= ''

    id = "WebSpadesProtocol"
    def doTick(self):
        print self.id

    def zzencode (self, message):
        binver = newmessage = ''

        for n in message:
            c = (int(self.zzencodechar( (ord(n)))))
            binver+=bin(c) + " "
            newmessage += chr(c)
        return newmessage, binver

    def zzdecode (self, message):
        newmessage = ''
        for n in message:
            c = ord(n)
            newmessage += str(self.zzdecodechar(c))
        return newmessage

    def zzdecodechar(self, value):
        """Inverse of zzencodechar()."""
        if not value & 0x1:
            return value >> 1
        return (value >> 1) ^ (~0)


    def zzencodechar(self, value):
        """ZigZag Transform:  Encodes signed integers so that they can be
        effectively used with varint encoding.  See wire_format.h for
        more details.
        """
        if value >= 0:
            return (value << 1)
        return (value << 1) ^ (~0)

    def encodeMessage(self, message):
        return message 

    def onConnect(self, request):
        wsport= (os.environ.get('PORT', 8080))

        #a = self.onConnectCallback(self)

        #a = self.onConnectCallback(self)
    def onOpen(self):
        self.client_id = str( hashlib.sha224(str(self)).hexdigest())
        print self.client_id
        print "****************"
        l = task.LoopingCall(self.runEverySecond)
        l.start(5.0)


    def onClose(self,reason,time,something):
        pass
        #a = self.onDisConnectCallback(self)

    def onPong(self, pong):
        self.pingtime = self.lastping-self.reactor.seconds()
        print( "pingtime:" + str(self.pingtime)) 

    def runEverySecond(self):
        self.lastping = self.reactor.seconds()
        self.sendPing()
        txt = "hello this is<b>sdasd</b> much better"
        mess, binver = self.zzencode(txt)
        tosend = self.encodeMessage(mess)   

        from StringIO import StringIO
        io = StringIO()
        json.dump([4,txt], io)
        s = io.getvalue()
        mess, binver = self.zzencode(s)
        self.sendMessage(mess, True)

        self.numberRequests+=1

    def onMessage(self, payload, isBinary):
        self.messages.append( Message(payload, self.reactor.seconds()) )


        try:
            json_object = json.loads(urllib.unquote((payload)))
            print str(isBinary) + str(json_object)

        except ValueError, e:
            print "INVALID PLOAD :" + str(isBinary) + "  " + (payload)


        #print "RECVD:" + str(len(self.messages)) 
        return 

class WebSpadesServerFactory(WebSocketServerFactory):
    isLeaf = True
    protocol = WebSpadesProtocol
    def render(self, request):
	    return

    def __del__(self):
        print "KILLED PROTO"
