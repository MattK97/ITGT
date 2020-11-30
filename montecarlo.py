


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

rows, columns = (10,10)
board = [[0 for i in range(columns)] for j in range(rows)]




def bestMove():
    tempBoard = None
    for k in range(100):
        if k%2 is 0 :
            tempBoard = monteCarloEvaluation(5, p1)
        else:
            tempBoard = monteCarloEvaluation(5, p2)
    for i in range(10):
        for j in range(10):
            if board[i][j] is 0:
                board[i][j] = tempBoard[i][j]
                break


def monteCarloEvaluation(nofSimulations, player):
    monteCaroChildTemp = board
    bestChild = None
    bestProbability = -1
    for n in range(numberOfLegalMoves):
        r = 0
        for k in range(nofSimulations):
            if checkOfWin is None:
                for i in range(10):
                    for j in range(10):
                        if monteCaroChildTemp[i][j] is 0:
                            monteCaroChildTemp[i][j] = player.color
                if heuristic > 0:
                    r += 1
        probability = r/nofSimulations
        if probability > bestProbability:
            bestChild = monteCaroChildTemp
            bestProbability = probability

        monteCaroChildTemp = board

    return bestChild


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

def numberOfLegalMoves():
    counter = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] is 0:
                counter += 1
    return counter*2

def checkOfWin():
    boardHeight = 10
    boardWidth = 10
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
    return None
