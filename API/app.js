const http = require('http') // need a file called http. Dependency: Code that other people wrote that now I am using
const hostname='127.0.0.1'; //this number is my own computer, meaning it is a fictional ip address = localhost
const port = 2450 //allows my computer to talk to server (abstract entry level), e.g. port 80 is http protocol

const server = http.createServer ( function(request, response){
    response.statusCode = 200; //used for communication, 200 means ok
    response.setHeader('Content-Type', 'text/plain');
    response.end('Wassup, sunshines');
});

server.listen(port, hostname, function(){
    console.log(`Server running at http://${hostname}:${port}/`)
})
