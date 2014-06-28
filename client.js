var fs = require('fs');
var Buffer = require('buffer').Buffer;
var net = require('net');

var HOST = 'localhost';
var PORT = 8000;
var IN_FILE = 'vid.h264'

var client = new net.Socket();

client.connect(PORT, HOST, function() {

    console.log('CONNECTED TO: ' + HOST + ':' + PORT);

    var content;
    fs.readFile(IN_FILE, 'binary', function (err, data) {

        if (err) {
            throw err;
        }

        client.write(data, 'binary');

        console.log(client.bufferSize);

        console.log(client.bytesWritten);

        client.end();
        client.destroy();

    }); 

});

client.on('data', function(data) {

    console.log('DATA: ' + data);
    client.destroy();

});

client.on('close', function() {
    console.log('Connection closed');
});
