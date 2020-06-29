from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import numpy as np 
from keras.preprocessing import image 
from PIL import Image
import pandas as pd
import itertools
import keras
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from keras.models import Sequential 
from keras import optimizers
from keras.layers import Dropout, Flatten, Dense 
from keras import applications 
from keras.utils.np_utils import to_categorical 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import math 
import datetime
import time
import os, sys

folderName = "Whole-Note"
datagen = ImageDataGenerator(
	rescale=1./ 255,
	shear_range=0.2,
	zoom_range=0.2,
	horizontal_flip=False)

path = "data/train/"
dirs = os.listdir(path)
for folder in dirs:
    newPath = path + folder
    dirs = os.listdir(newPath)
    for item in dirs:
        file = newPath+"/"+item
        if os.path.isfile(file):
            img = load_img(file)
            x = img_to_array(img)
            x = x.reshape((1,) + x.shape)
            i = 0
            for batch in datagen.flow(x, batch_size=1,save_to_dir=newPath+"/", save_prefix=item, save_format='jpeg'):
                i += 1
                if i > 15:
                    break