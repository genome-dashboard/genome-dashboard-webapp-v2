console.log('Interpreting: dashboard/scripts/dashboard.js.')

var serverurl = window.location.href;
console.log(serverurl);

serverurl = serverurl.substring(0, serverurl.lastIndexOf('/'));
console.log(serverurl);

var posting = $.post("SRC/jason/sessionsacCer3.php");
console.log(posting);

posting.done(function(data){
  var n = data.length;
  var sessionpage = serverurl.substring(0, serverurl.lastIndexOf('sessions'));
  sessionpage = sessionpage + "sessions/" + data.replace(/"/g,'') +"/icmgb-dna.html";

  var chromatinpage = serverurl + "/sessions/" + data.replace(/"/g,'') +"/chromatin.html";

  window.open(chromatinpage,'JsmolChromatin','width=500,height=500');
  location.replace(sessionpage);
});
