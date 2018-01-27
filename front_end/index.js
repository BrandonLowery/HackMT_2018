var express   = require("express");
var mysql     = require('mysql');

var app       = express();

var con = mysql.createConnection({
  host: "104.198.251.11",
  user: "jared",
  password: "humphries",
  database: "data"
});
var car_count;
var lot_max;
var lot = "kom";



con.connect(function(err){
  if(err) throw err;
  con.query("SELECT car_count FROM LOT_INFO WHERE lot_name = 'kom'", function(err, result, fields){
    if(err) throw err;
    car_count = JSON.stringify(result[0].car_count);

  });
  console.log(car_count);


});



// var pool      = mysql.createPool({
//     connectionLimit: 100,
//     host      :   '104.198.251.11',
//     user      :   'jared',
//     password  :   'humphries',
//     database  :   'data',
//     debug     :   false
// });
//
// function handle_database(req, res){
//   pool.getConnection(function(err,connection){
//            if (err) {
//              connection.release();
//              res.json({"code" : 100, "status" : "Error in connection database"});
//              return;
//            }
//
//            console.log('connected as id ' + connection.threadId);
//
//            connection.query("select * from user",function(err,rows){
//                connection.release();
//                if(!err) {
//                    res.json(rows);
//                }
//            });
//
//            connection.on('error', function(err) {
//                  res.json({"code" : 100, "status" : "Error in connection database"});
//                  return;
//            });
//      });
// }
//
// app.get("/", function(req, res){
//     handle_database(req,res);
// });


app.listen(3000);
