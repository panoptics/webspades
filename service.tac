# -*- coding: iso-8859-1 -*-
""" sim runs independantly of network """
__all__ = ["perf_counter"]

import ctypes, os, time, sys

from twisted.web import server, resource
from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import protocol, reactor, task
from twisted.application import service, internet
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile

from autobahn.twisted.choosereactor import install_reactor
from autobahn.twisted.websocket import WebSocketServerFactory, \
                                       WebSocketServerProtocol
from autobahn.twisted.resource import WebSocketResource
from twisted.manhole import telnet

from webspades import WebSpadesServerFactory,WebSpadesProtocol
from simulation import sim
from livecoding import reloader, namespace
from core.connection import conn, Register

port= int(os.environ.get('PORT', 8080))

CLOCK_MONOTONIC_RAW = 4 # see <linux/time.h>

class timespec(ctypes.Structure):
    _fields_ = [
        ('tv_sec', ctypes.c_long),
        ('tv_nsec', ctypes.c_long)
    ]

if os.name == 'posix':
    librt = ctypes.CDLL('librt.so.1', use_errno=True)
    clock_gettime = librt.clock_gettime
    clock_gettime.argtypes = [ctypes.c_int, ctypes.POINTER(timespec)]


if os.name == 'nt':
    def _win_perf_counter():
        if _win_perf_counter.frequency is None:
            _win_perf_counter.frequency = _time.QueryPerformanceFrequency()
        return _time.QueryPerformanceCounter() / _win_perf_counter.frequency
    _win_perf_counter.frequency = None

def perf_counter():

    if perf_counter.use_performance_counter:
        try:
            return _win_perf_counter()
        except OSError:
            # QueryPerformanceFrequency() fails if the installed
            # hardware does not support a high-resolution performance
            # counter
            perf_counter.use_performance_counter = False

    if perf_counter.use_monotonic:
        # The monotonic clock is preferred over the system time
        try:
            return time.monotonic()
        except OSError:
            perf_counter.use_monotonic = False

    if perf_counter.use_raw_monotonic:
        CLOCK_MONOTONIC_RAW = 4 # see <linux/time.h>
        # The raw monotonic clock is used becuase it has no NTP 
        # adjustments
        try:
            t = timespec()
            if clock_gettime(CLOCK_MONOTONIC_RAW , ctypes.pointer(t)) != 0:
                errno_ = ctypes.get_errno()
                raise OSError(errno_, os.strerror(errno_))
            return t.tv_sec + t.tv_nsec * 1e-9
        except OSError:
            perf_counter.use_raw_monotonic = False

    # Fall back to sys time
    return time.time()

perf_counter.use_performance_counter = (os.name == 'nt')
perf_counter.use_monotonic = hasattr(time, 'monotonic')
perf_counter.use_raw_monotonic = (perf_counter.use_monotonic == False)

from twisted.conch import manhole_tap


def getWebService():
    #reactor = install_reactor()
    #print("Running on reactor {}".format(reactor))
    factory1 = WebSpadesServerFactory("ws://localhost:" + str(port),
                                     debug = False,
                                     debugCodePaths = False)
    resource1 = WebSocketResource(factory1)
    


    root = File("./htdocs/")
    root.putChild("ws", resource1)
    site = Site(root)
    server = reactor.listenTCP(port, site)
    reactor.seconds = perf_counter

    factory1.protocol.reactor = reactor

    conn.__init__(reactor, factory1.protocol, server)
    sim.__init__(reactor, factory1.protocol, server, conn, 5.0)
    sim.onConnectionCallback = conn.onConnectCallback
    sim.start()
    return server

application = service.Application("webspades")
manhole_tap.makeService({"telnetPort": "tcp:6023",
                         "sshPort": "tcp:6022",
                         "namespace": {"foo": "bar"},
                         "passwd": "passwd"}).setServiceParent(application)
                         
#logfile = DailyLogFile("webspades.log", "/tmp")
#application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

# attach the service to its parent application
service = getWebService()
#service.setServiceParent(application)





def loadScripts():
    print("load scripts")
    script_objects = []
    script_names = ["run"]
    modules = []
    for script in script_names[:]:
        try:
            module = __import__('scripts.%s' % script, globals(), locals(), 
                [script])
            script_objects.append(module)
        except ImportError, e:
            print "(script '%s' not found: %r)" % (script, e)
            script_names.remove(script)

    for script in script_objects:
        if "apply_script" in dir(script):
            script.apply_script()
        else:
            script_objects.remove(script)

#loadScripts()


def GetCurrentDirectory():
    # There's probably a better way of doing this.
    dirPath = os.path.dirname(__file__)
    if not len(dirPath):
        dirPath = sys.path[0]
    return dirPath

def GetScriptDirectory():
    parentDirPath = GetCurrentDirectory()
    return os.path.join((parentDirPath), "scripts")
scriptnum =0 
scriptDirPath = GetScriptDirectory()

global Register
cr = reloader.CodeReloader(mode=reloader.MODE_OVERWRITE, callback=conn.CB )


scriptDirectory = cr.AddDirectory("scripts", scriptDirPath)
