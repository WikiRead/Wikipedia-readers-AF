const mongoose = require('mongoose');
var Schema = new mongoose.Schema;
const DataSchema = mongoose.Schema({
    id : {
    type: String,
    required: true
  },
  timestamp: {
    type: Number,
    required: true
  },
  gazeX: {
    type: [Number],
    required: true
  },
  gazeY: {
      type: [Number],
      required: true
  },
  image:{
      type: String,
      required: true
  }
 
});

const Data = mongoose.model('Data', DataSchema);

module.exports = Data;