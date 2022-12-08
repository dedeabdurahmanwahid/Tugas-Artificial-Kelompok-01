import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2

from keras.datasets import mnist
objects=mnist
(train_img,train_lab),(test_img,test_lab)=objects.load_data()

from google.colab import drive
drive.mount('/content/drive')

plt.imshow(train_img[0])
print(train_lab[0])

for i in range(20):
  plt.subplot(4,5,i+1)
  plt.imshow(train_img[i],cmap='gray_r')
  plt.title("Digit : {}".format(train_lab[i]))
  plt.subplots_adjust(hspace=0.5)
  plt.axis('off')