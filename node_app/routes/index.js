var express = require('express');
const Data = require('../models/data');
const request = require('request');

var router = express.Router();





/* GET home page. */
router.get('/', function(req, res, next) {
  
  res.render("main",{ myVar : "Typhoon Goni (2020)" })
});

router.get('/temp', (req, res) => {
  var temp = "q";
  //console.log(req);
  request(
    { url: "https://en.wikipedia.org/w/api.php?action=opensearch&search="+req.query.search+"&format=json" },
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
      res.render("main",{ myVar : temp })
    }
  )
  
});

router.post('/', function(req,res,next){
  console.log(typeof req.body.image);
  console.log("data posted")
  Data.create({
    id: req.body.deviceId, timestamp: req.body.timestamp, gazeX: req.body.gazeX, gazeY: req.body.gazeY, image: req.body.image 
  })
  res.send(req.body);
});




module.exports = router;
