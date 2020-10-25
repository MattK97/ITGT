from random import randint
import numpy as np
import os

clear = lambda:os.system('cls')


class Player:
    lastPlaced = None
    danger = 0
    def __init__(self, name, color, inf, isMaxing):
        self.name = name
        self.color = color
        self.inf = inf
        self.isMaxing = isMaxing

p1 = Player("John", "B", np.inf, True)
p2 = Player("Jane", "R", -np.inf, False)
endGame = False

rows, columns = (10,10)
board = [[0 for i in range(columns)] for j in range(rows)]

def checkOfWin():
    boardHeight = 10
    boardWidth = 10
    winner = None
    # poziom
    for y in range(boardHeight):
        for x in range(boardWidth - 5):
            if equals5(board[x][y], board[x+1][y], board[x+2][y], board[x+3][y], board[x+4][y]):
                return board[x][y]

    # pion
    for x in range(boardWidth):
        for y in range(boardHeight - 5):
            if equals5(board[x][y], board[x][y+1], board[x][y+2], board[x][y+3], board[x][y+4]):
                return board[x][y]

    # /
    for x in range(boardWidth - 5):
        for y in range(5, boardHeight):
            if equals5(board[x][y], board[x+1][y-1], board[x+2][y-2], board[x+3][y-3], board[x+4][y-4]):
                return board[x][y]

    # \
    for x in range(boardWidth - 5):
        for y in range(boardHeight - 5):
            if equals5(board[x][y], board[x+1][y+1], board[x+2][y+2], board[x+3][y+3], board[x+4][y+4]):
                return board[x][y]

    freeSpots = 0
    for i in range(10):
        for j in range(10):
            if(board[i][j]==0):
                freeSpots += 1

    if winner is None and freeSpots == 0:
        return "tie"
    else:
        return winner


def bestMove(player):
    bestScore = player.inf
    move = []
    for i in range(10):
        for j in range(10):
            if(board[i][j] == 0):
                board[i][j] = player.color
                score = minimax(board, 5, player.isMaxing)
                board[i][j] = 0
                if player.isMaxing is False:
                    if score > bestScore:
                        bestScore = score
                        move = (i,j)
                else:
                    if score < bestScore:
                        bestScore = score
                        move = (i,j)

    print(move)
    board[move[0]][move[1]] = player.color

scores = {"B" : 10, "R": -10, "tie": 0}



def equals2(a,b):
    return a==b and a!=0
def equals3(a, b, c):
    return a==b and b==c and a!=0
def equals4(a,b,c,d):
    return a==b and b==c and c==d and a!=0
def equals5(a,b,c,d,e):
    return a==b and b==c and c==d and d==e and a!=0


def heuristic():
    score = 0
    for i in range(10):
        for j in range(10):
###############################################################
            if i<9 and equals2(board[i][j], board[i+1][j]):
                if board[i][j] == "R":
                    score+=20
                else:
                    score-=20

            if j<9 and equals2(board[i][j], board[i][j+1]):
                if board[i][j] == "R":
                    score+=20
                else:
                    score-=20

            if i<9 and j<9 and equals2(board[i][j], board[i+1][j-1]):
                if board[i][j] == "R":
                    score+=20
                else:
                    score-=20

            if i<9 and j<9 and equals2(board[i][j], board[i+1][j+1]):
                if board[i][j] == "R":
                    score+=20
                else:
                    score-=20
###########################################################################
            if i<8 and equals3(board[i][j], board[i+1][j], board[i+2][j]):
                if board[i][j] == "R":
                    score+=80
                else:
                    score-=80
            if j<8 and equals3(board[i][j], board[i][j+1], board[i][j+2]):
                if board[i][j] == "R":
                    score+=80
                else:
                    score-=80

            if i<8 and j<8 and equals3(board[i][j], board[i+1][j-1], board[i+2][j-2]):
                if board[i][j] == "R":
                    score+=80
                else:
                    score-=80

            if i<8 and j<8 and equals3(board[i][j], board[i+1][j+1], board[i+2][j+2]):
                if board[i][j] == "R":
                    score+=80
                else:
                    score-=80
#################################################################################
            if i<7 and equals4(board[i][j], board[i+1][j], board[i+2][j], board[i+3][j]):
                if board[i][j] == "R":
                    score+=160
                else:
                    score-=160
            if j<7 and equals4(board[i][j], board[i][j+1], board[i][j+2],board[i][j+3]):
                if board[i][j] == "R":
                    score+=160
                else:
                    score-=160

            if i<7 and j<7 and equals4(board[i][j], board[i+1][j-1], board[i+2][j-2],board[i+3][j-3]):
                if board[i][j] == "R":
                    score+=160
                else:
                    score-=160

            if i<7 and j<7 and equals4(board[i][j], board[i+1][j+1], board[i+2][j+2],board[i+3][j+3]):
                if board[i][j] == "R":
                    score+=160
                else:
                    score-=160
######################################################################################
            if i<6 and equals5(board[i][j], board[i+1][j], board[i+2][j], board[i+3][j], board[i+4][j]):
                if board[i][j] == "R":
                    score+=640
                else:
                    score-=640
            if j<6 and equals5(board[i][j], board[i][j+1], board[i][j+2],board[i][j+3], board[i][j+4]):
                if board[i][j] == "R":
                    score+=640
                else:
                    score-=640

            if i<6 and j<6 and equals5(board[i][j], board[i+1][j-1], board[i+2][j-2],board[i+3][j-3], board[i+4][j-4]):
                if board[i][j] == "R":
                    score+=640
                else:
                    score-=640

            if i<6 and j<6 and equals5(board[i][j], board[i+1][j+1], board[i+2][j+2],board[i+3][j+3],board[i+4][j+4]):
                if board[i][j] == "R":
                    score+=640
                else:
                    score-=640

#########################################################################################
    return score


def minimax(board, depth, isMaximizing):
    if depth==0:
        return heuristic()

    if isMaximizing:
        bestScore = -np.inf
        for i in range(10):
            for j in range(10):
                if board[i][j] == 0:
                    board[i][j] = "B"
                    score = minimax(board, depth-1, False)
                    board[i][j] = 0
                    bestScore = max(score, bestScore)
                    return bestScore
    else:
        bestScore = np.inf
        for i in range(10):
            for j in range(10):
                if board[i][j] == 0:
                    board[i][j] = "R"
                    score = minimax(board, depth-1, True)
                    board[i][j] = 0
                    bestScore = min(score, bestScore)
                    return bestScore


for i in range(100):
    print(i)
    print(np.array(board))
    print("\n")
    if checkOfWin() is not None:
        if i%2 == 0 :
            print("R wygrywa")
        else:
            print("B wygrywa")
        break
    if i%2==0:
        bestMove(p1)
    else:
        bestMove(p2)
