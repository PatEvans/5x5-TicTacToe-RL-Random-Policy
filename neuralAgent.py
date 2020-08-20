import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from gameRules import *

def calcValue(boards,model):
    #tensorBoards=np.array(boards).reshape(-1,4,4,1)
    tensorBoards= np.array(boards).reshape((-1, 25))
    #tensorBoards = tf.convert_to_tensor(tensorBoards,dtype=tf.int32)
    prediction=model.predict(tensorBoards)
    #print(prediction)
    return prediction

def neuralMove(model,board,player):
    children=getChildren(board,player)
    #+ve value for cross win
    #-ve value for noughts win

    maxVal=-100000

    maxIndex=-1
    valArray=calcValue(children,model)
    for i in range(0,len(children)):
        if(player==1):
            current=valArray[i][0]-valArray[i][1]
            if(current>maxVal):
                maxVal=current
                maxIndex=i
        elif(player==2):
            current=valArray[i][1]-valArray[i][0]
            if(current>maxVal):
                maxVal=current
                maxIndex=i

    if(maxVal<0):
        maxVal=-100000
        for i in range(0,len(children)):
            if(player==1):
                current=valArray[i][2]-valArray[i][1]
                if(current>maxVal):
                    maxVal=current
                    maxIndex=i
            elif(player==2):
                current=valArray[i][2]-valArray[i][0]
                if(current>maxVal):
                    maxVal=current
                    maxIndex=i
    board=children[maxIndex]

    return board
