from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dinosong3plets!'
app.config['MYSQL_DB'] = 'chroma_match'

db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

#registrasi pengguna
@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    
    try:
        cursor = db.cursor()
        
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)

        db.commit()
        cursor.close()
        
        return jsonify({'message': 'Registration Success'})
    except mysql.connector.Error as error:
        return jsonify({'message': 'Registration Failed!', 'error': str(error)})


#login pengguna
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    try:
        cursor = db.cursor()
    
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        
        user = cursor.fetchone()
        
        cursor.close()
        
        if user:
            return jsonify({'message': 'Login Success'})
        else:
            return jsonify({'message': 'Login Failed!'})
    except mysql.connector.Error as error:
        return jsonify({'message': 'Login Failed!', 'error': str(error)})


#mendapatkan data jenis warna kulit
@app.route('/skin-colors', methods=['GET'])
def get_skin_colors():
    try:
        cursor = db.cursor()
       
        query = "SELECT id, name FROM skin_colors"
        cursor.execute(query)
        
        skin_colors = cursor.fetchall()

        cursor.close()

        skin_colors_data = [{'id': color[0], 'name': color[1]} for color in skin_colors]

        return jsonify(skin_colors_data)
    except mysql.connector.Error as error:
        return jsonify({'message': 'Failed!', 'error': str(error)})


from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('./Model.h5')

#mendapatkan rekomendasi outfit berdasarkan warna kulit
@app.route('/outfit-recommendation', methods=['POST'])
def get_outfit_recommendation():
    # Menerima file gambar yang diunggah oleh pengguna
    if 'image' not in request.files:
        return jsonify({'message': 'No Image'})
    
    image_file = request.files['image']
    
    # Membaca gambar menggunakan PIL
    try:
        outfit_image = Image.open(image_file)
    except:
        return jsonify({'message': 'Failed!'})
    
    # Preprocessing gambar outfit
    outfit_image = outfit_image.resize((224, 224))
    outfit_array = np.array(outfit_image) / 255.0
    outfit_array = np.expand_dims(outfit_array, axis=0)
    
    # Prediksi menggunakan model machine learning
    outfit_prediction = model.predict(outfit_array)
    
    # Decode prediksi menjadi kelas atau label yang sesuai
    outfit_label = decode_prediction(outfit_prediction)
    
    outfit_recommendations = [{'id': 1, 'outfit': outfit_label}]
    return jsonify(outfit_recommendations)


#History
@app.route('/prediction-history', methods=['GET'])
def get_prediction_history():
    try:
        cursor = db.cursor()
        query = "SELECT * FROM outfit_recommendations"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        # Mengonversi hasil query menjadi format yang sesuai
        prediction_history = []
        for row in result:
            prediction = {'id': row[0], 'color': row[1], 'outfit': row[2]}
            prediction_history.append(prediction)

        return jsonify(prediction_history)
    except mysql.connector.Error as error:
        return jsonify({'message': 'Failed!', 'error': str(error)})


#data pengguna
@app.route('/user', methods=['GET'])
def get_user():
    token = request.headers.get('Authorization')

    try:
        cursor = db.cursor()
        query = "SELECT username, token FROM users WHERE token = %s"
        values = (token,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()

        if result is None:
            return jsonify({'message': 'Token tidak valid'})
        
        user_data = {'username': result[0], 'token': result[1]}

        return jsonify(user_data)
    except mysql.connector.Error as error:
        return jsonify({'message': 'Failed!', 'error': str(error)})


if __name__ == '__main__':
    app.run()
