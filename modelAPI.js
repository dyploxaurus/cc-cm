const fetch = require('node-fetch');

function callModelAPI(data) {
  const apiUrl = 'https://api-model.com/predict'; // Ganti dengan URL API model.h5 terpisah

  fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ data }), // Sesuaikan dengan format data yang dibutuhkan oleh API model.h5
  })
    .then(response => response.json())
    .then(result => {
      // Tangani hasil respons dari API model.h5 di sini
      console.log(result);
    })
    .catch(error => {
      // Tangani error jika permintaan gagal
      console.error(error);
    });
}

module.exports = { callModelAPI };
