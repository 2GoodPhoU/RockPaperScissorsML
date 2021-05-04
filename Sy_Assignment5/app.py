#https://www.godo.dev/tutorials/python-http-server-client/
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from flask import Flask, jsonify, request
from PIL import Image
from datetime import datetime

app = Flask(__name__)
project_name = "Rock, Paper and Scissors image classification server."
project_owner = "Eric Sy"
now = datetime.now()
host="0.0.0.0"
port="80"

@app.route("/")
def home():
	print(project_name)
	print(project_owner)
	print("Host: " + host)
	print("Port: " + port)
	print(now)
	text = project_name + '\n' + project_owner + '\n' + "Host: " + host + '\n' + "Port: " + port + '\n' + now.strftime("%d/%m/%Y %H:%M:%S")
	return text

@app.route("/ml", methods=["POST"])
def process_image():
	print(project_name)
	print(project_owner)
	print("Host: " + host)
	print("Port: " + port)
	print(now)
	text = project_name + '\n' + project_owner + '\n' + "Host: " + host + '\n' + "Port: " + port + '\n' + now.strftime("%d/%m/%Y %H:%M:%S")

	file = request.files['image']
	#img = Image.open(file.stream)
	model = load_model('model.h5')

	path = file
	img = image.load_img(path, target_size=(150, 150))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	images = np.vstack([x])
	classes = model.predict(images, batch_size=10)
	if(np.allclose(classes,np.array([1, 0, 0]))):
		text = text + '\n' + "The image you’ve submitted is classified as a: paper"
	if(np.allclose(classes,np.array([0, 1, 0]))):
		text = text + '\n' + "The image you’ve submitted is classified as a: rock"
	if(np.allclose(classes,np.array([0, 0, 1]))):
		text = text + '\n' + "The image you’ve submitted is classified as a: scissors"
	return text


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=80)
