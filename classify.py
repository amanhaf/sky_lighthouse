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

Elliptical = "An elliptical galaxy is a type of galaxy with an approximately ellipsoidal shape and a smooth, nearly featureless image. They are one of the three main classes of galaxy described by Edwin Hubble in his Hubble sequence and 1936 work The Realm of the Nebulae, along with spiral and lenticular galaxies.\n Elliptical (E) galaxies are, together with lenticular galaxies (S0) with their large-scale disks, and ES galaxies with their intermediate scale disks, a subset of the 'early-type' galaxy population."

Spiral = "Spiral galaxies form a class of galaxy originally described by Edwin Hubble in his 1936 work The Realm of the Nebulae and, as such, form part of the Hubble sequence. Most spiral galaxies consist of a flat, rotating disk containing stars, gas and dust, and a central concentration of stars known as the bulge. These are often surrounded by a much fainter halo of stars, many of which reside in globular clusters. "

def classify(name):
    
    img = image.load_img(os.path.join(image_directory, name) , target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes =  model_j.predict(images)
    clist= classes.tolist()[0]
        
    if clist[0] == 1.0:
        print("Elliptical")
        return "<h3>Elliptical</h3><br><br>"+ Elliptical
    if clist[1] == 1.0:
        print("Lenticular")
        return "Lenticular"
    elif clist[2] == 1.0:
        print("Spiral\n"+Spiral)
        return "Spiral\n"+ Spiral

