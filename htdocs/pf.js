/*
* vendorPrefix.js - Copyright(c) Addy Osmani 2011.
* http://github.com/addyosmani
* Tests for native support of a browser property in a specific context
* If supported, a value will be returned.
*/
function igP(prp, c) {
    return (prp in c);
}

function gP(prp, c) {
 
    var vp = ['moz', 'webkit', 'khtml', 'o', 'ms'],
        u = prp.charAt(0) + prp.slice(1),
        prf, len = vp.length, q = null;

    while (len--) {
        q = vp[len];
        q = (c.toString().indexOf('style')) 
            ? q.charAt(0)+ q.slice(1):q;
        prf = ((q + u) in c) ? (q) : prf;
    }
    prf = (prp in c) ? prp : undefined;
    return (prf) ? prf.toLowerCase() : "--" + prp;
}
// Localstore set/del test
function lsTest(){
    var t = 0;
    try {
        localStorage.setItem(t, t);
        localStorage.removeItem(t);
        return true;
    } catch(e) {
        return false;
    }
}

function doPF() {
    $C = function(id){return document.createElement(id);}
    var tres = [
        (gP('hidden', document)),
        (gP('transform', $C('div').style)),
        (gP('transition', $C('div').style)),
        (gP('FileReader', window)),
        (gP('WebSocket', window)),
        (gP('Worker', window)),
        (gP('requestAnimationFrame', window)),
        (gP('WebGLRenderingContext', window))
    ];
    for (t in tres){
        console.log(tres[t]);
    }

    if (igP('localStorage', window) ){
        if(lsTest() === true){
            console.log("localStorage");
        }else{
            console.log("localStorage OFF");
        }
    }
}