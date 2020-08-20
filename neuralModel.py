import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from formatData import *

class neuralModel(object):
    def __init__(self):
        self.model=Sequential()
    def createModel(self):

          self.model.add(Dense(200, activation='relu', input_shape=(25, )))
          self.model.add(Dropout(0.2))
          self.model.add(Dense(125, activation='relu'))
          self.model.add(Dense(75, activation='relu'))
          self. model.add(Dropout(0.1))
          self. model.add(Dense(25, activation='relu'))
          self. model.add(Dense(3, activation='softmax'))
          self. model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['acc'])

    def trainModel(self,trainingData):
        tensorData=compileToTensor(trainingData)
        x=tensorData[0]
        y=tensorData[1]
        print(x)
        print(y)

        self.model.fit(x,y,batch_size=256,epochs=10,validation_split=0.1,shuffle=True,use_multiprocessing=True,workers=8,verbose=1)
