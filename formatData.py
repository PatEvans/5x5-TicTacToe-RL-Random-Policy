import numpy as np
import os
from keras.utils import to_categorical
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
#trainingData consists of a number of game, result pairs
#it formats these pairs into tensors for the neural network
def compileToTensor(trainingData):
    x=[]
    y=[]
    n=len(trainingData[0][0][0])

    for i in range(0, len(trainingData)):
        result=trainingData[i][1]
        for j in range(0, len(trainingData[i][0])):
            x.append(trainingData[i][0][j])
            y.append(result)


    x = np.array(x).reshape((-1, 25))


    y=to_categorical(y)
    return [x,y]
