 const mysql = require('mysql');

//buat koneksi database
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'dinosong3plets!',
    database: 'chroma_match',
    port: '3306'
  });
  

  connection.connect((err) => {
    if (err) {
      console.error('Error connecting to database:', err);
      return;
    }
    console.log('Connected to database.');
  });
  

module.exports = conn;