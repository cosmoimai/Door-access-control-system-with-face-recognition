const express = require("express")
const http = require('http');
const bodyParser = require("body-parser")
const fs = require("fs")
// const hostname = '127.0.0.1';
const port = process.env.PORT || 3000;

var doorstate = false

const app = express();

// middleware
app.use(express.json());
app.use(express.urlencoded());

//firebase
var FCM = require('fcm-node');
var serverKey = 'AAAALrt0o7s:APA91bHvefiklFxxP49e3nAvVp4_iDzAtkLy3Okdn5VbwXtOFEpyY_TUOwkun8V9hLVGfeKhy0inZrBu09pcNYo1L9WDzGd5R30fAQFXGfb28GbrBm4XLStHpmR5hIVB5aEsFLROPJe1';
var fcm = new FCM(serverKey);


app.get("/", function (req, res) {
  //console.log("here")
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello ld');
})

var base64
var buffer
const topicName = 'Door Lock System';

app.post("/send", async function (req, res) {
  console.log("here")
  // console.log(req.body.file)
  base64 = req.body.file
  // console.log(base64)
  buffer = Buffer.from(base64, "base64");
  // var num1 = Number(req.body.num1);
  // var num2 = Number(req.body.num2);

  // var result = num1 + num2 ;
  fs.writeFileSync("new-path.jpg", buffer);

  var filepath = __dirname + '/new-path.jpg'
  var message = {
    to: 'eZtIS8tFSR2ZMBglv2Efhe:APA91bFn6ceW5emp4vWUzRY3HqDXhhSkOadH58zrLPAmL-LeskA6nuUC-3A0FMaHQtXrHOOx_15HIBqsIjM6Mu7fBNcH8W7lLbgqyoz5y-fygo_adgss6MMVrl9MEqfGKbcx-2Hglb-x',

    data: {
      "type": "mytype",
      "title": "My Title",
      "body": "https://iot-door-lock-system.herokuapp.com/img"
    },
    notification: {
      title: 'An Intruder Wants To Enter',
      body: 'https://iot-door-lock-system.herokuapp.com/img',
      image: 'https://iot-door-lock-system.herokuapp.com/img'
    },
    topic: topicName
  };

  fcm.send(message, function (err, response) {
    if (err) {
      console.log("Something has gone wrong!" + err);
      console.log("Respponse:! " + response);
    } else {
      // showToast("Successfully sent with response");
      console.log("Successfully sent with response: ", response);
    }
  });
  //   getMessaging().send(message)
  // .then((response) => {
  //   // Response is a message ID string.
  //   console.log('Successfully sent message:', response);
  // })
  // .catch((error) => {
  //   console.log('Error sending message:', error);
  // });

  res.send("Add");
});

app.get("/img", function (req, res) {
  var filepath = __dirname + '/new-path.jpg'
  console.log(filepath)
  res.sendFile(filepath);
})

app.get("/doorstate", function (req, res) {
  if (doorstate) {
    res.send({
      msg: "YES"
    })
  } else {
    res.send({
      msg: "NO"
    })
  }
  // res.send(filepath);
})

app.post("/changedoorstate", function (req, res) {
  var temp = req.body.msg
  console.log(temp)
  // res.send("getting")
  if (temp == "YES") {
    doorstate = true
    // console.log("this is doorstate "+doorstate)
    res.send({
      msg: "YES"
    })
  } else {
    doorstate = false
    res.send({
      msg: "NO"
    })
  }


})

// const server = http.createServer((req, res) => {
//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/plain');
//   res.end('Hello aaaaqsld');
// });

app.listen(port, () => {
  console.log(`Server running at port ${port}/`);
});