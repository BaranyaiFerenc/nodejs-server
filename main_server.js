
var http = require('http');
var fs = require('fs');

http.createServer(function (req, res) {
    fs.readFile('html/demopage.html', function(err, data) {
        if(err){
            res.writeHead(404, {'Content-Type': 'text/html'});
            return res.end('<html><body style="background-color: rgb(173, 83, 83);"><h1 style="color: white; text-align: center; margin-top: 25%; font-size: xx-large;">ERROR 404</h1><h3 style="color: white; text-align: center;">The searched page not found!</h3></body></html>');
        }

        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);

        return res.end();
    });
    
}).listen(8080);