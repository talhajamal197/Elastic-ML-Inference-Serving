# app.py
from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        image_bytes = file.read()
        label = predict(image_bytes)
        return jsonify({'label': label})
    except IOError:
        return jsonify({'error': 'Cannot open image'}), 400

@app.route('/', methods=['GET'])
def hello_endpoint():
    return('Hello world')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
