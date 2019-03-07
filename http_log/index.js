var express = require('express');
var app = express();
const fs = require('fs');

app.get('/', function (req, res) {
  fs.appendFile("log.txt", JSON.stringify({'status': 'connected', 'time': new Date().getTime(), 'params': req.query}) + '\n', function(err) {
    if(err) {
        return console.log(err);
    } else {
      res.json({'message': 'succesful!'});
    }
   });
});

app.listen(4000, function () {
  console.log('App started on port 4000!');
});
