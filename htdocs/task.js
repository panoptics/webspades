importScripts('varint/zzcode.js');
importScripts('./util.js');
var oversize=0;
self.decodeBinMessage = function(e){
    /!-- Sanitize here --!/
    if (e.byteLength>MAX_BUFFER) return 'oversize';
    var b = new Uint8Array(e);
    if (b.length>MAX_BUFFER) return 'oversize';
    var dv = new DataView(b.buffer);

    var op =''
    for (var i=0;i<b.length;i++){
      var c = dv.getUint8(i, true);
      op+= String.fromCharCode( zzdecode(c) );
    }

    return decodeURIComponent(escape(removeTags(op)));
}

self.addEventListener('message', function(e) {
  var data = e.data;
  switch (data.cmd) {
    case ct.PROCESS:
      self.processMessage(data.msg);
    break;
    default:
      self.postMessage('Unknown command: ' + data.cmd);
  };
}, false);

self.processMessage = function(message){
   var txt='';
   var text = self.decodeBinMessage(message);

   try
   {
      var transformed = JSON.parse((text));
      
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
      txt="Error in decode packet: len:" + text;
   }
  self.postMessage((text));

}







/*
expect = 5;//randint(0x7FFFFFFF);
var arr = new Uint32Array([ (123),zzencode(23000)]);

encoded = encode(arr[0]);
var expect2 = zzencode( (expect).toString(8) );
var data = zzdecode(decode(encoded));

console.log(decode.bytesRead, " enc len :" + encoded.length, " enc data: " + encoded, data, arr[0]);


function randint(range) {
  return ~~(Math.random() * range) ; 
}*/