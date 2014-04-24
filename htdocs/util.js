var MAX_BUFFER = 1024
$ = function(id){return document.getElementById(id)}
$C = function(id){return document.createElement(id)}
$CT = function(id){return document.createTextNode(id)}
var mt = {
    RED : 0,
    ALERT : 3,
    MESSAGE : 4
}
var ct = {
    PROCESS : 1
}
chr = function(a){ return String.fromCharCode(a) }
var tagBody = '(?:[^"\'>]|"[^"]*"|\'[^\']*\')*';
var tagOrComment = new RegExp(
    '<(?:'
    + '!--(?:(?:-*[^->])*--+|-?)'
    + '|script\\b' + tagBody + '>[\\s\\S]*?</script\\s*'
    + '|style\\b' + tagBody + '>[\\s\\S]*?</style\\s*'
    + '|/?[a-z]'
    + tagBody
    + ')>',
    'gi')

function removeTags(html) {
  var oldHtml;
  do {
    oldHtml = html
    html = html.replace(tagOrComment, '')
  } while (html !== oldHtml);
  return html.replace(/</g, '&lt;')
}


