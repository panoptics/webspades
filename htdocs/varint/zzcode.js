<!-- ZigZag encode/decode a string !-->
"use strict";

(function(zz, undefined){

   zz.zzencode = function(n){return (n << 1) ^  (n >> 31);};
   zz.zzdecode = function(n){return (n >> 1) ^ -(n  & 1 );};

   var MAX_BUFFER = 2048;

   zz.apply = function(a, codec, enc ){
      if (a.length>MAX_BUFFER) {return '';}
      var hex='', i=0, trans;
      trans = (enc) ? function(a){return codec(a.charCodeAt(0)); } : function(a){return codec(a);};

      for (i in a ) {
         hex += chr( trans(a[i]) );
      }
      return hex;
   };
   zz.decodezzstring = function(a){
      return zz.apply(a, zz.zzdecode, false);
   };
   zz.encodezzstring = function(a){
      return zz.apply(a, zz.zzencode, true);
   };
   zz.decodezzbin = function(e){
       if (e.byteLength>MAX_BUFFER) {return 'oversize';}
       var dv = new DataView(b.buffer), o=c='', i=0;
       for (i in b){
         c = dv.getUint8(i, true);
         o+= chr( zz.zzdecode(c) );
       }
       return decodeURIComponent(escape(removeTags(o)));
   };
})( this.zz = this.zz || {} );