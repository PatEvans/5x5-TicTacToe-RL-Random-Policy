from gameRules import *
from random import *
from randomAgent import *
import copy

def randomData(board):
    originalBoard=copy.deepcopy(board)
    games=[]
    for i in range(10000):
        games.append(randGame(board))
        board=copy.deepcopy(originalBoard)
    return games

def randGame(board):
    game=[]
    game.append(copy.deepcopy(board))
    while(terminate(board)==-1):
        randMove(board,1)
        game.append(copy.deepcopy(board))
        if(terminate(board)!=-1):
            break
        randMove(board,2)
        game.append(copy.deepcopy(board))
    result=terminate(board)
    return [game,result]
