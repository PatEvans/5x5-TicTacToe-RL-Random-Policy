from randomTrain import *
from neuralModel import *
from testModel import *


n = 5
board = [[0 for i in range(n)] for j in range(n)]
neural=neuralModel()
neural.createModel()
option=input("Do you want to train a model or load a model? ( t / l )")

if(option=="t"):
    #produce training data via random policy
    trainingData=randomData(board)
    #and train neural model using the data produced
    neural.trainModel(trainingData)
    neural.model.save('RandomModel.h5')

else:
    from tensorflow import keras
    neural.model=keras.models.load_model('RandomModel.h5')

    print("Loaded!")
#test the model
board = [[0 for i in range(n)] for j in range(n)]
randomTest(neural.model,board)
