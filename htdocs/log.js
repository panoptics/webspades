"use strict";

(function(global) {
    var global = (function(){ return this || (1,eval)('this') })();


    var log = {
        debug : console.log,
        warn  : console.log
    };

    global.log = log;

    // now we can use the log property of the global object to reach our log object.
}());