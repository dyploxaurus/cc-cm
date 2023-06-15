'use strict';

var response = require('./res');
var connection = require('./connect');

exports.getHistory = function (req, res) {
    connection.query('SELECT * FROM history', function (error, rows, fields) {
        if (error) {
            response.error("Failed to fetch history data", res);
        } else {
            response.ok(rows, res);
        }
    });
};

exports.getPrediction = function (req, res) {
    connection.query('SELECT * FROM prediction', function (error, rows, fields) {
        if (error) {
            response.error("Failed to fetch prediction data", res);
        } else {
            response.ok(rows, res);
        }
    });
};

exports.getSkinColor = function (req, res) {
    connection.query('SELECT * FROM skin_color', function (error, rows, fields) {
        if (error) {
            response.error("Failed to fetch skin color data", res);
        } else {
            response.ok(rows, res);
        }
    });
};

exports.getUsers = function (req, res) {
    connection.query('SELECT * FROM user', function (error, rows, fields) {
        if (error) {
            response.error("Failed to fetch user data", res);
        } else {
            response.ok(rows, res);
        }
    });
};

