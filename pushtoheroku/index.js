var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require("cors");
var app = express();

app.use(express.json());
app.use(cors());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.get('/', function (req, res) {
  res.send("hello! welcome to the backend!");
});

app.post('/python', async (req, res) => {
  const { spawn } = require('child_process');
  const pythonProcess = spawn('python', ['./main.py', req.body.id]);
  pythonProcess.stdout.on('data', (data) => {
    res.send(JSON.stringify({width: data.toString()}));
  });

  pythonProcess.stderr.on('data', (data) => {
    res.send(JSON.stringify({error: data.toString()}));
  });
});

// error handler
const port = process.env.PORT || 8000
app.listen(port, () => {});
