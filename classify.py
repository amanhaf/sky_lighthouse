import pandas as pd
import os, random, shutil

import tensorflow as tf
import keras_preprocessing
from keras.callbacks import EarlyStopping
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

image_directory = '/Volumes/Seagate/Local-DSI/Capstone/webapp/static/uploads'
model = tf.keras.models.load_model('my_model.h5')

def classify(name):
    
    img = image.load_img(os.path.join(image_directory, name) , target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images)
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

