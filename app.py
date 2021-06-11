from flask import Flask
from flask.globals import request
from PIL import Image
from io import BytesIO
from flask.helpers import send_file

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "hellow world Mario Paucar Oscanoa, es un buen día "

@app.route('/ping')
def ping():
    return "pong"

@app.route('/cat.jpg')
def cat():
    width = request.args.get('width')
    height = request.args.get('height')

    size = (int(width),int(height))

    img = Image.open('gato.jpg')
    img.thumbnail(size)
    img_io = BytesIO()
    img.save(img_io,"JPEG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")