'use strict';

const express = require('express');
const router = express.Router();
const jsonku = require('./controller');
const modelAPI = require('./modelAPI');
const axios = require('axios');


// Mengambil data history dari tabel history
router.get('/history', (req, res) => {
  const query = 'SELECT * FROM history';

  connection.query(query, (error, rows) => {
    if (error) {
      console.error('Error executing query:', error);
      response.error('Failed to retrieve history data', res);
    } else {
      response.ok(rows, res);
    }
  });
});

// Mengambil data prediction dari tabel prediction
router.get('/prediction', (req, res) => {
  const query = 'SELECT * FROM prediction';

  connection.query(query, (error, rows) => {
    if (error) {
      console.error('Error executing query:', error);
      response.error('Failed to retrieve prediction data', res);
    } else {
      response.ok(rows, res);
      const data = prepareData(rows);
      modelAPI.callModelAPI(data);
    }
  });
});

// Mengambil data skin_color dari tabel skin_color
router.get('/skin_color', (req, res) => {
  const query = 'SELECT * FROM skin_color';

  connection.query(query, (error, rows) => {
    if (error) {
      console.error('Error executing query:', error);
      response.error('Failed to retrieve skin_color data', res);
    } else {
      response.ok(rows, res);
    }
  });
});

// Mengambil data user dari tabel user
router.get('/user', (req, res) => {
  const query = 'SELECT * FROM user';

  connection.query(query, (error, rows) => {
    if (error) {
      console.error('Error executing query:', error);
      response.error('Failed to retrieve user data', res);
    } else {
      response.ok(rows, res);
    }
  });
});

module.exports = router;
