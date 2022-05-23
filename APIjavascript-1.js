var userName = "DCHBKYZF5NMXHCV8AG4M1J53DFDONO8Z";
var passWord = "WV0KBNNCRLP0SO3CYZMOGFQATYTPG2Y";

{/* <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
 */}

var XMLHttpRequest = require('xhr2');
var xhr = new XMLHttpRequest();
//const fetch = require("node-fetch");


console.log("Hello World");

function authenticateUser(user, password)
{
    var token = user + ":" + password;

    // Should i be encoding this value????? does it matter???
    // Base64 Encoding -> btoa
    var hash = btoa(token); 

    return "Basic " + hash;
}

var settings = {
    "url": "HTTPS:////api.limblecmms.com:443/v2/tasks/?limit=5",
    "method": "GET",
    "timeout": 0,
    "headers": {
      "Authorization": "authenticateUser(userName, passWord)"
    },
  };
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });


/* 
var myHeaders = new fetch.Headers();
myHeaders.append("Authorization", "authenticateUser(userName, passWord)");
                                //authenticateUser(userName, passWord) , Basic e3thcGlVTn19Ont7YXBpUGFzc319

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("HTTPS:////api.limblecmms.com:443/v2/tasks/?limit=5", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
 */

/* function CallWebAPI() {

    // New XMLHTTPRequest
    var request = new XMLHttpRequest();
    request.open("POST", "https://xxx123.caspio.com/oauth/token", false);
    request.setRequestHeader("Authorization", authenticateUser(userName, passWord));  
    request.send();
    // view request status
    alert(request.status);
    response.innerHTML = request.responseText;
} */


/* var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("GET", "HTTPS:////api.limblecmms.com:443/v2/tasks/?limit=5");
xhr.setRequestHeader("Authorization", "Basic e3thcGlVTn19Ont7YXBpUGFzc319");

xhr.send(); */