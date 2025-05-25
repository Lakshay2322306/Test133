from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend on Vercel to access

@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})

@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run()
