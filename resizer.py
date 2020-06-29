#!/usr/bin/python
from PIL import Image
import pandas as pd
import numpy as np 
import itertools
import keras
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img 
from keras.models import Sequential 
from keras import optimizers
from keras.preprocessing import image
from keras.layers import Dropout, Flatten, Dense 
from keras import applications 
from keras.utils.np_utils import to_categorical 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import math 
import datetime
import time
import os, sys

def resize():
	path = "data/train/"
	dirs = os.listdir(path)
	for folder in dirs:
		newPath = path + folder
		dirs = os.listdir(newPath)
		for item in dirs:
			file = newPath+"/"+item
			if os.path.isfile(file):
				im = Image.open(file)
				f, e = os.path.splitext(file)
				f = "data/preview/"+ f.split("data/train/")[1]
				# Cambiar tamanio de imagen
				imResize = im.resize((50,150), Image.ANTIALIAS)
				imResize.save(f + '.png', 'PNG', quality=90)
resize()
