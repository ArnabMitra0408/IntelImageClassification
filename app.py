from flask import Flask, render_template, redirect, request

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
import json
import pickle
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Model, load_model
import tensorflow

classes={0:'buildings',1:'forest',2:'glacier',3:'mountain',4:'sea',5:'street'}
model_resnet = load_model('resnet50.h5')

def predictimage(img):
    img = image.load_img(img, target_size=(224,224,3))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    prediction=model_resnet.predict(img)[0]
    
    x=np.array(prediction)
    z=np.argmax(x)

    return classes[z]


# In[15]:




# __name__ == __main__
app = Flask(__name__)


@app.route('/')
def hello():
	return render_template("index.html")


@app.route('/', methods= ['POST'])
def marks():
	if request.method == 'POST':

		f = request.files['userfile']
		path = "./static/{}".format(f.filename)# ./static/images.jpg
		f.save(path)

		prediction=predictimage(path)
		
		result_dic = {
		'image' : path,
		'prediction' : prediction
		}

	return render_template("index.html", your_result =result_dic)

if __name__ == '__main__':
	# app.debug = True
	app.run(debug = True)