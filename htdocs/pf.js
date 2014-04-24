//function igP(e,t){return e in t}function gP(e,t){var n=["moz","webkit","khtml","o","ms"],r=e.charAt(0)+e.slice(1),i,s=n.length,o=null;while(s--){o=n[s];o=t.toString().indexOf("style")?o.charAt(0)+o.slice(1):o;i=o+r in t?o:i}i=e in t?e:undefined;return i?i.toLowerCase():"--"+e}function lsTest(){var e=0;try{localStorage.setItem(e,e);localStorage.removeItem(e);return true}catch(t){return false}}function doPF(){$C=function(e){return document.createElement(e)};var e=[gP("hidden",document),gP("transform",$C("div").style),gP("transition",$C("div").style),gP("FileReader",window),gP("WebSocket",window),gP("Worker",window),gP("requestAnimationFrame",window),gP("WebGLRenderingContext",window)];for(t in e){console.log(e[t])}if(igP("localStorage",window)){if(lsTest()===true){console.log("localStorage")}else{console.log("localStorage OFF")}}}
/*
* vendorPrefix.js - Copyright(c) Addy Osmani 2011.
* http://github.com/addyosmani
* Tests for native support of a browser property in a specific context
* If supported, a value will be returned.
*/
pollyFill = function(){
    'use strict';
    function igP(prp, c){return (prp in c)}

    function gP(prp, c){
        var vp = ['moz', 'webkit', 'khtml', 'o', 'ms'],
            u = prp.charAt(0) + prp.slice(1),
            prf, len = vp.length, q = null

        while (len--) {
            q = vp[len]
            q = (c.toString().indexOf('style')) 
                ? q.charAt(0)+ q.slice(1):q
            prf = ((q + u) in c) ? (q) : prf
        }
        prf = (prp in c) ? prp : undefined;
        return (prf) ? prf.toLowerCase() : "--" + prp
    }
    // Localstore set/del test
    function lsTest(){
        var t = 0;
        try {
            localStorage.setItem(t, t)
            localStorage.removeItem(t)
            return true
        } catch(e) {
            return false
        }
    }

    function doPF(){
        var w = window, d = document
        $C = function(id){return d.createElement(id)}
        
        var tres = [
            (gP('hidden', d)),
            (gP('transform', $C('div').style)),
            (gP('transition', $C('div').style)),
            (gP('FileReader', w)),
            (gP('WebSocket', w)),
            (gP('Worker', w)),
            (gP('requestAnimationFrame', w)),
            (gP('WebGLRenderingContext', w))
        ]
        for (var t in tres){
            //console.log(tres[t])
        }

        if (igP('localStorage', window) ){
            if(lsTest() === true){
                console.log("localStorage")
            }else{
                console.log("localStorage OFF")
            }
        }
        return tres
    }
    return doPF()
}
self.pollyFill()