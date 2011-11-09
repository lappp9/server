
function post (msg) 
{
    var req = new XMLHttpRequest (); 
    req.open ('POST', 'http://127.0.0.1:8000'); 

    req.onreadystatechange = function (aEvt) { 
        if (req.readyState == 4) {
            if (req.status !== 200) {
                alert ("error talking to RPC server"+req.status);
            }
        }
    }; 

    var xmlrpcrequest = "<?xml version='1.0'?>" + 
                        "<methodCall><methodName>setMessage</methodName>" + 
                        "<params><param><value><string>" + msg + 
                        "</string></value></param></params></methodCall>"; 
	alert(JSON.stringify(xmlrpcrequest));
    req.send (xmlrpcrequest); 
}
