<!-- ZigZag encode/decode a string !-->
"use strict";
(function(global){
   var global = (function(){ return this || (1,eval)('this') })();
   /* ... Code that defines MyModule ... */
   global.zz = global.zz || {};
   global.zz.zzencode = function(n){return (n << 1) ^  (n >> 31);}
   global.zz.zzdecode = function(n){return (n >> 1) ^ -(n  & 1 );}

   var MAX_BUFFER = 2048;

   global.zz.decodezzstring = function(a){
      if (a.length>MAX_BUFFER) return;
      var hex='';
      for (var c in a ) {
         hex += String.fromCharCode( zz.zzdecode(a[c].charCodeAt(0)) );
      }
      return hex;
   }
   global.zz.encodezzstring = function(a){
      if (a.length>MAX_BUFFER) return;
      var hex='';
      for (var c in a ) {
         hex += String.fromCharCode( zz.zzencode(a[c].charCodeAt(0)) );
      }
      return hex
   }
})(this);