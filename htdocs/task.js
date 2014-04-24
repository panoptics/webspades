importScripts('./util.js');
importScripts('./varint/zzcode.js');
 
var oversize=0;


self.addEventListener('message', function(e) {
  var data = e.data;
  switch (data.cmd) {
    case ct.PROCESS:
      self.processMessage(data.msg);
      break;
    default:
      self.postMessage('Unknown command: ' + data.cmd);
      break;
  }
}, false);

self.processMessage = function(message){
   var transformed=txt='',
  global = (function(){ return this;})();
   try
   {
      text = global.zz.decodezzbin(message);
      transformed = JSON.parse((text));
      
      switch (transformed[0]){
         case 1:
         case 2:
         case mt.ALERT:
            txt = "ALERT !!";
         case mt.MESSAGE:
            txt += transformed[1];
            break; 
         default:
            txt = "Unknown packet";
            break;
      }
   }catch(err){
      txt="Error in decode packet: len:";
   }
  self.postMessage(txt);
};
