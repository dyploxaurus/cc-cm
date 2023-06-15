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
        
        return jsonify({'message': 'Registrasi pengguna berhasil'})
    except mysql.connector.Error as error:
        return jsonify({'message': 'Registrasi pengguna gagal', 'error': str(error)})


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
            return jsonify({'message': 'Login berhasil'})
        else:
            return jsonify({'message': 'Login gagal'})
    except mysql.connector.Error as error:
        return jsonify({'message': 'Login gagal', 'error': str(error)})


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
        return jsonify({'message': 'Gagal mendapatkan data jenis warna kulit', 'error': str(error)})


# Import library atau modul yang diperlukan
import tensorflow as tf
# ...
# Import library atau modul lain yang diperlukan

# Load model machine learning
model = tf.keras.models.load_model('')

#mendapatkan rekomendasi outfit berdasarkan warna kulit
@app.route('/outfit-recommendation', methods=['POST'])
def get_outfit_recommendation():
    skin_color_id = request.json['skin_color_id']
    
    try:
        cursor = db.cursor()
        query = "SELECT name FROM skin_colors WHERE id = %s"
        values = (skin_color_id,)
        cursor.execute(query, values)
        skin_color = cursor.fetchone()[0]
        cursor.close()
        
        #prediksi menggunakan model machine learning
        # ...
        #dengan menggunakan model machine learning
        
        outfit_recommendations = [{'id': 1, 'color': 'Red', 'outfit': 'Dress'}, {'id': 2, 'color': 'Blue', 'outfit': 'Jeans'}]
        return jsonify(outfit_recommendations)
    except mysql.connector.Error as error:
        return jsonify({'message': 'Gagal mendapatkan rekomendasi outfit', 'error': str(error)})


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
        return jsonify({'message': 'Gagal mendapatkan riwayat prediksi', 'error': str(error)})


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
        return jsonify({'message': 'Gagal mendapatkan data pengguna', 'error': str(error)})


if __name__ == '__main__':
    app.run()
