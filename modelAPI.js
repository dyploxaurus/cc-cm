const axios = require('axios');

function callModelAPI(data) {
  const apiUrl = 'https://chromamatch.up.railway.app/'; // Ganti dengan URL API model.h5 terpisah

  axios.post(apiUrl, { data }, { headers: { 'Content-Type': 'application/json' } })
    .then(response => {
      // Tangani hasil respons dari API model.h5 di sini
      const result = response.data;
      console.log('Hasil prediksi:', result);
      // Lakukan tindakan selanjutnya dengan hasil prediksi
    })
    .catch(error => {
      if (error.response) {
        console.error('Error respons:', error.response.data);
      } else if (error.request) {
        console.error('Tidak ada respons:', error.request);
      } else {
        console.error('Error:', error.message);
      }
    });
}

module.exports = { callModelAPI };
