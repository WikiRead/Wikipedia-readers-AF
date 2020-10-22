var express = require('express');
const Data = require('../models/data');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  
  res.render("../views/main.ejs")
});

router.post('/', function(req,res,next){
  console.log(typeof req.body.image);
  Data.create({
    title: req.body.title, timestamp: req.body.timestamp, gazeX: req.body.gazeX, gazeY: req.body.gazeY, image: req.body.image 
  })
  res.send(req.body);
});

module.exports = router;
