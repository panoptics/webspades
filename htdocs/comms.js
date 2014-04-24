"use strict";

(function(global){
  var global = (function(){ return this || (1,eval)('this') })();
  /* ... Code that defines MyModule ... */
  global.comms = global.comms || {};
  //global.comms.doInit = (global.module || {}).exports = global.comms.doInit;
  global.comms.doInit = function(){

    var worker = new Worker('task.js'), connection = null;

    if ('WebSocket' in window){
         /* WebSocket is supported. You can proceed with your code*/
      //sheltered-meadow-7230.herokuapp.com:
      connection = new WebSocket('ws://192.168.0.6:8080/ws',["pi","po"])
      connection.binaryType = "arraybuffer"
    } else {
    }

    global.comms.notify = function(txt){
      var txtNode = $CT(txt), br = $C('br'), mdiv = $('messages')
      mdiv.appendChild(txtNode)
      mdiv.appendChild(br)
    }

    worker.addEventListener('message', function(e) {
      console.log(e.data)
       comms.notify( (e.data) )
    }, false)

    global.comms.dologin = function(message){
     if ( message.p && message.u ){

        var jsms = (JSON.stringify(message)),
          buffer = new Uint8Array(jsms.length),
          dv = new DataView(buffer.buffer),
          op = '', en ='', res='', resg='', i=0, c=''

        for (i=0;i<jsms.length;i++){
          c = (jsms[i].charCodeAt(0))
          dv.setUint8(i, c , true)
          op+= String.fromCharCode( zz.zzencode(c))
        }
        comms.notify(res.length + " :en: " + (op))
        for (i=0;i<jsms.length/4;i++){
          en += (encode(dv.getUint32(i*4, true)))
        }
        res = en.split(","); 
        for (i in res){
          c =  parseInt(res[i], res[i].length/8 ).toString(10)
          resg+=(String.fromCharCode(c))
        }
        //var res2 = zz.encodezzstring(res.join("")); 
        comms.notify(res.length + " :en: " + (resg))
        
        //for (var i in res){console.log(res[i])}

        en =''
        for (i=0;i<jsms.length;i++){
          en += String.fromCharCode((dv.getUint8(i,true)));
        }
        comms.notify((en).length + " :en: " + encodeURIComponent(en))
/* 
        comms.notify(op.length + " :op: " +op)
        var escpd =encodeURIComponent(escape(zz.encodezzstring(jsms)))
        comms.notify(escpd.length + " :escpd: " + escpd)

        var unescpd = zz.decodezzstring(op)
        comms.notify(unescpd.length + " :unescpd: " + unescpd)

        comms.notify( jsms.length + " :jsms: " +jsms)*/
        try{
           connection.send(dv.buffer)
        }catch(err){
           notify("Login not sent")
        }     
     }else{
        comms.notify("Supply credentials")
     }
    }
    connection.onmessage = function(e){
       if (typeof e.data == "string") {
       } else {
          worker.postMessage( {'cmd':ct.PROCESS,'msg': e.data}  )
       }
    }
    connection.onopen = function(){
       /*Send a small message to the console once the connection is established */
       console.log('Connection open!')
       comms.dologin({'p':78986,'u':5678,'v':[0.546546,546465,56560]})
    }
  }

 comms.doInit()
})();