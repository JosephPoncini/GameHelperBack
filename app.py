from flask import Flask, jsonify, request
from flask_cors import CORS
from services.wordleService import get_wordle_data
from services.wordHuntService import get_word_hunt_data

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api/wordle_get_data', methods=['POST'])
def wordle_get_data():
    data = request.get_json()  # Get JSON data from request body
    word = data.get('word')
    code = data.get('code')
    word_bank = data.get('word_bank')
    result = get_wordle_data(word, code, word_bank)  # Process the data
    return jsonify(result)  # Return the result as a JSON response

@app.route('/api/word_hunt_get_data', methods=['POST'])
def word_hunt_get_data():
    data = request.get_json()  # Get JSON data from request body
    board = data.get('board')
    result = get_word_hunt_data(board)  # Process the data
    return jsonify(result)  # Return the result as a JSON response

if __name__ == '__main__':
    app.run(debug=True)
