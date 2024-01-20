from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/data', methods=['GET'])
def get_data():
    # You can retrieve data from a database, perform calculations, etc.
    data = {"key": "value"}
    return jsonify(data)
