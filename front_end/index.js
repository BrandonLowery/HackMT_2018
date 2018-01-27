var mysql      = require('mysql');
 var connection = mysql.createConnection({
   host     : '104.198.251.11',
   user     : 'jared',
   password : 'humphries',
   database:  'data'
 });
 connection.connect(function(err){
   if(err) throw err;
   console.log("Connected!");
 });

 connection.query('SELECT * from LOT_INFO', function(err, rows, fields) {
   if (!err)
     console.log('The solution is: ', rows);
   else
     console.log('Error while performing Query.');
 });

 connection.end();
