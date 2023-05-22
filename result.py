import numpy as np
import cv2
import os
import random
import tensorflow as tf


h,w = 512,512
num_cases = 3

model = tf.keras.models.load_model('model')

lowSevere = 1
midSevere = 2
highSevere = 4

def image_to_res(f):
    print(f)
    test_img = cv2.imread(f)
    resized_img = cv2.resize(test_img,(w,h))
    resized_img = resized_img/255
    cropped_img = np.reshape(resized_img,
          (1,resized_img.shape[0],resized_img.shape[1],resized_img.shape[2]))

    test_out = model.predict(cropped_img)

    test_out = test_out[0,:,:,0]*1000
    test_out = np.clip(test_out,0,255)

    resized_test_out = cv2.resize(test_out,(test_img.shape[1],test_img.shape[0]))
    resized_test_out = resized_test_out.astype(np.uint16)

    test_img = test_img.astype(np.uint16)

    grey = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    for i in range(test_img.shape[0]):
     for j in range(test_img.shape[1]):
          if(resized_test_out[i,j]>40):
            test_img[i,j,0]=test_img[i,j,0] + resized_test_out[i,j]
            resized_test_out[i,j] = highSevere
          else:
            resized_test_out[i,j] = 0

    M = cv2.moments(resized_test_out)
    maxMomentArea = resized_test_out.shape[1]*resized_test_out.shape[0]*highSevere
    print("0th Moment = " , (M["m00"]*100/maxMomentArea), "%")

    test_img = np.clip(test_img,0,255)

    test_img = test_img.astype(np.uint8)
    test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
    return test_img
