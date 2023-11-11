from flask import Flask, request
import numpy as np 
import base64
from flask_cors import CORS
import cv2, io

app = Flask(__name__)
CORS(app)

def decode_base64_image(data):
    base64_image = data
    base64_data = base64_image.split(',')[1]
    image_data = base64.b64decode(base64_data)
    image_bytes = io.BytesIO(image_data).read()
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

@app.route('/feed', methods = ['POST'])
def hello_world():  # put application's code here
    data = request.get_json()
    decode_base64_image(data.get("imageDataURL"))
    return data

if __name__ == '__main__':
    app.run()
