import pandas as pd
import os, random, shutil

import tensorflow as tf
import tensorflow.keras.preprocessing
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

image_directory = './static/uploads'
#Reading the model from JSON file
with open('model.json', 'r') as json_file:
    json_savedModel= json_file.read()
#load the model architecture
model_j = tf.keras.models.model_from_json(json_savedModel)
model_j.load_weights('weights.h5')

def classify(name):
    
    img = image.load_img(os.path.join(image_directory, name) , target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes =  model_j.predict(images)
    clist= classes.tolist()[0]
        
    if clist[0] == 1.0:
        print("Elliptical")
        return "Elliptical"
    if clist[1] == 1.0:
        print("Lenticular")
        return "Lenticular"
    elif clist[2] == 1.0:
        print("Spiral")
        return "Spiral"

