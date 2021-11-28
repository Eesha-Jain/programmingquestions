let express = require('express');
let app = express();

app.get('/', function (req, res) {
  res.sendFile('/index.html', {root:'.'});
});

app.get('/python', function(req, res) {
    const spawn = require('child_process').spawn;
    const process = spawn('python', ['./python/sum.py', req.query.num1, req.query.num2]);
    process.stdout.on('data', (data) => {
        res.send(JSON.stringify({sum: data.toString()}));
    });
})

const port = process.env.PORT || 8080
app.listen(port, () => {
  console.log("Server ran!") 
});