zzencode = function(n){return (n << 1) ^  (n >> 31);}
zzdecode = function(n){return (n >> 1) ^ -(n  & 1 );}
var MAX_BUFFER = 2048;

decodezzstring = function(a){
   var hex='';
   for (var i = 0; i < a.length && i<2048; i++) {
      hex += String.fromCharCode( zzdecode(a[i].charCodeAt(0)) );
   }
   return hex;
}
encodezzstring = function(a){
   var hex='';
   for (var i = 0; i < a.length && i<2048; i++) {
      hex += String.fromCharCode( zzencode(a[i].charCodeAt(0)) );
   }
   return hex
}