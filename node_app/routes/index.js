var express = require('express');
const Data = require('../models/data');
const request = require('request');

var router = express.Router();





/* GET home page. */
router.get('/', function(req, res, next) {
  
  res.render("main",{ myVar : "HomePage" })
});

router.post('/temp', (req, res) => {
  var temp = "q";
  console.log(req.body);
  request(
    { url: "https://en.wikipedia.org/w/api.php?action=opensearch&search="+req.body.search+"&format=json" },
    (error, response, body) => {
      if (error || response.statusCode !== 200) {
        return res.status(500).json({ type: 'error', message: err.message });
      }
      //console.log(response.headers);
      //console.log(response);
      console.log("inside")
      var wiki = JSON.parse(body);
      temp = wiki[1][0]
      //console.log("work")
      console.log(temp)
      //res.send(wiki)
      res.send(temp)
    }
  )
  
});

router.post('/', function(req,res,next){
  console.log(typeof req.body.image);
  
  
  console.log(req.body.url)
  
  Data.create({
    sysId: req.body.sysId,
    sessionId: req.body.sessionId,
    timestamp: req.body.timestamp,
    gazeX: req.body.gazeX,
    gazeY: req.body.gazeY,
    image: req.body.image ,
    url : req.body.url
  })
  console.log("data posted")
  res.send(req.body);
});




module.exports = router;
