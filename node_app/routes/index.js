var express = require('express');
const Data = require('../models/data');
const request = require('request');

var router = express.Router();





/* GET home page. */
router.get('/', function(req, res, next) {
  
  res.render("../views/main.ejs")
});

router.get('/temp', (req, res) => {
  var temp = 2;
  request(
    { url: 'http://localhost:4000/json_placeholder' },
    (error, response, body) => {
      if (error || response.statusCode !== 200) {
        return res.status(500).json({ type: 'error', message: err.message });
      }
      console.log(response.headers);
      console.log(response);
      temp = response;
      res.json(JSON.parse(body));
    }
  )

  res.send(temp)
});

router.post('/', function(req,res,next){
  console.log(typeof req.body.image);
  Data.create({
    title: req.body.title, timestamp: req.body.timestamp, gazeX: req.body.gazeX, gazeY: req.body.gazeY, image: req.body.image 
  })
  res.send(req.body);
});




module.exports = router;
