'use strict';

exports.ok = function(values, res){
    var data = {
        'status':200,
        'values':values
    };

    console.log(values);
    res.json(data);
    res.end();

    callModelAPI(values);
};

exports.error = function(message, res){
    var data = {
        'status':400,
        'message': message
    };

    console.error(message);
    res.json(data);
    res.end();
};
  