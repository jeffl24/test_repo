// console.log("Hello");
// var https = require("https")

var url = 'https://api.tradegecko.com/variants';
var token = 'f4855aebc4a92c0d6a09f07b105bcbae81afbaf8cb1344f47a5b5c45cf8f4c1e';
  
// var options = {headers: { Authorization: 'Bearer ' + token }};

// var response = https.get(url, options);

// var result = JSON.parse(response.responseText());
// console.log(result);

const request = require('request');

request(
    {
        url: url,
        headers : {
            'Authorization' : token
        }
    },
    (err, res, body) => {
    if (err) { return console.log(err); }
    res    
    
);

