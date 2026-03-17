from flask import Flask, request, jsonify
from flask_cors import CORS
from model import detect_ai_image
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Truth Lens API Running"

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image']

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    result = detect_ai_image(path)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)