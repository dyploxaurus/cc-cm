const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const axios = require('axios');
const modelAPI = require('./modelAPI');


//parse application/json
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

const routes = require('./router');
app.use('/', routes);
app.get('/', (req, res) => {
    res.send('Hello, world!');
  });
  

app.listen(3001, () => {
    console.log('Server started on port 3001');
});
