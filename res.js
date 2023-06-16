'use strict';

exports.ok = function(values, res){
    var data = {
        'status':200,
        'values':values
    };

    console.log(values);
    res.json(data);
    res.end();

    // Panggil API yang menggunakan model di sini
    callModelAPI(values); // Panggil fungsi yang melakukan permintaan ke API yang menggunakan model
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

function callModelAPI(data) {
    // Lakukan permintaan ke API yang menggunakan model di sini
    // Gunakan pustaka seperti 'fetch' atau 'axios' untuk melakukan permintaan HTTP

    // Contoh penggunaan 'fetch' untuk mengirim permintaan POST ke URL API yang menggunakan model
    const apiUrl = 'https://chromamatch.up.railway.app/';

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(result => {
            // Tangani hasil respons dari API yang menggunakan model di sini
            console.log(result);
        })
        .catch(error => {
            // Tangani error jika permintaan gagal
            console.error(error);
        });
}
