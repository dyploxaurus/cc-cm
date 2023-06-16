const axios = require('axios');

function callModelAPI(data) {
  const apiUrl = 'https://chromamatch.up.railway.app/';

  axios.post(apiUrl, { data }, { headers: { 'Content-Type': 'application/json' } })
    .then(response => {

      const result = response.data;
      console.log('Hasil prediksi:', result);
    })
    .catch(error => {
      if (error.response) {
        console.error('Error respons:', error.response.data);
      } else if (error.request) {
        console.error('No respons:', error.request);
      } else {
        console.error('Error:', error.message);
      }
    });
}

module.exports = { callModelAPI };
