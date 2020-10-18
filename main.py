from random import randint
import numpy as np


class Player:
    lastPlaced = None
    danger = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color

p1 = Player("John", "B")
p2 = Player("Jane", "R")

endGame = False

rows, columns = (10,10)
board = [[0 for i in range(columns)] for j in range(rows)]


#######################################################################################################################################################
def newTurn(player, opponent):
    if player.lastPlaced is None:
        randomRow = randint(0,9)
        randomColumn = randint(0,9)
        board[randomRow][randomColumn] = player.color
        player.lastPlaced = (randomRow, randomColumn)
    else:
        if(opponent.danger <= 1):
            newCoordinates = checkForOpportunities(player.lastPlaced, player)
            board[newCoordinates[0]][newCoordinates[1]] = player.color
            player.lastPlaced = newCoordinates
        else:
            newCoordinates = checkForOpportunities(opponent.lastPlaced, player)
            board[newCoordinates[0]][newCoordinates[1]] = player.color
            player.lastPlaced = newCoordinates
    return 0


def checkForOpportunities(lastPlaced, player):
    if  lastPlaced[0]-1 >= 0 and board[lastPlaced[0]-1][lastPlaced[1]] == 0:
        player.danger += 1
        return (lastPlaced[0]-1, lastPlaced[1])

    elif lastPlaced[0]+1 <= 9 and board[lastPlaced[0]+1][lastPlaced[1]] == 0:
        player.danger += 1
        return (lastPlaced[0]+1, lastPlaced[1])

    elif lastPlaced[1]-1 >= 0 and board[lastPlaced[0]][lastPlaced[1]-1] == 0:
        player.danger += 1
        return (lastPlaced[0], lastPlaced[1]-1)

    elif lastPlaced[1]+1 >= 9 and board[lastPlaced[0]][lastPlaced[1]+1] == 0:
        player.danger += 1
        return (lastPlaced[0], lastPlaced[1]+1)

    else:
        for a in range(10):
            if 0 in board[a]:
                b = board[a].index(0)
                return (a,b)



def checkOfWin(board, tile):
    boardHeight = 10
    boardWidth = 10
    # poziom
    for y in range(boardHeight):
        for x in range(boardWidth - 5):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile and board[x+4][y] == tile and board[x+5][y] == tile:
                return True

    # pion
    for x in range(boardWidth):
        for y in range(boardHeight - 5):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile and board[x][y+4] == tile and board[x][y+5] == tile:
                return True

    # /
    for x in range(boardWidth - 5):
        for y in range(5, boardHeight):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile and board[x+4][y-4] == tile and board[x+5][y-5] == tile:
                return True

    # \
    for x in range(boardWidth - 5):
        for y in range(boardHeight - 5):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile and board[x+4][y+4] == tile and board[x+5][y+5] == tile:
                return True
    return False



#####################################################################################################################################################################################

def createRandomBoard():
    totalCounter = 0
    for i in range(10):
        counter = 0
        for i in range(1000):
            l = np.array(['R','B'])
            k = l[np.random.randint(0, len(l), (10, 10))]
            unique, counts = np.unique(k, return_counts=True)
            if abs(counts[0]- counts[1]) <=1:
                counter += 1
        totalCounter +=counter
    print("************************")
    print("Metoda druga")
    print("Poprawnych symulacji w 10 tysiącach prób: " + str(totalCounter))
    print("Wynik: " +  str(totalCounter/10) + "100^3 = " + str((totalCounter/10)*(100**3)))
######################################################################################################################################################################################






maxNumberOfMoves = 100
numberOfMoves = 0;
numberOfMovesInParty=0
numberOfCurrentlyPossibleMoves = 100
totalNumberOfCurrentlyPossibleMovesInParty=0
totalNumberOfCurrentlyPossibleMovesInProbe=0


for k in range(1000):
    board = [[0 for i in range(columns)] for j in range(rows)]
    numberOfMovesInParty=0
    totalNumberOfCurrentlyPossibleMovesInParty=0
    numberOfCurrentlyPossibleMoves = 100
    for i in range(maxNumberOfMoves):
        numberOfMovesInParty+=1
        totalNumberOfCurrentlyPossibleMovesInParty += numberOfCurrentlyPossibleMoves
        if i%2 == 0 and not checkOfWin(board, p1.color):
            newTurn(p1,p2)
            numberOfCurrentlyPossibleMoves-=1
        elif i%2 != 0 and not checkOfWin(board, p2.color):
            newTurn(p2,p1)
            numberOfCurrentlyPossibleMoves-=1
        else:break

    numberOfMoves += numberOfMovesInParty
    totalNumberOfCurrentlyPossibleMovesInProbe += totalNumberOfCurrentlyPossibleMovesInParty



branching = (totalNumberOfCurrentlyPossibleMovesInProbe/1000)/(numberOfMoves/1000)
sredniaRuchow = numberOfMoves/1000
print("************************")
print("Metoda pierwsza")
print("branching: " + str(branching))
print("depth: " + str(sredniaRuchow))
print("Zlozonosc: " + str(branching**sredniaRuchow))
createRandomBoard()
