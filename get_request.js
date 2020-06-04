//fetch using a Request and a Headers objects
//using jsonplaceholder for the data
const fetch = require("node-fetch");
const axios = require("axios")

var variants_url = 'https://api.tradegecko.com/variants';
var token = 'f4855aebc4a92c0d6a09f07b105bcbae81afbaf8cb1344f47a5b5c45cf8f4c1e';

var options = {
    method: "GET", 
    headers: { Authorization: 'Bearer ' + token }
    };
let object
fetch(variants_url, options)
.then(result => result.json())
.then(res => {
    object = res.variants[1]
    // do something with object
})

// if (response.ok) { // if HTTP-status is 200-299
//   // get the response body (the method explained below)
//   let json = response.json();
//   console.log(json);
// } else {
//   console.log("HTTP-Error: " + response.status);
// }

// Working fetch
// var response = fetch(variants_url, options).then(response => response.json() ).then( data => console.log(data['variants'][0]));