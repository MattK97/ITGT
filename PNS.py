root = {
"board": "",
"proof": 1,
"disproof": 1,
"expanded": False,
"type": "AND",
"value": 0
}

rows, columns = (10,10)
board = [[0 for i in range(columns)] for j in range(rows)]

def PNS(root):
    evaluate(root)
    setProofAndDisproofNumbers(root)
    current = root
    while root.proof is not 0 and root.disproof is not 0 and resourcesAvailable():
        mostProving = selectMostProvingNode(current)
        expandNode(mustProving)
        current = updateAncestors(mostProving, root)

def setProofAndDisproofNumbers(node):
    if node.expanded:
        if node.type is "AND":
            node.proof = 0
            node.disproof = 1000000 #ma być np.inf
            for child in node.children:
                node.proof += child.proof
                node.disproof = min(node.disproof, child.disproof)
        if node.type is "OR":
            node.proof = 1000000
            node.disproof = 0
            for child in node.children:
                node.disproof += child.disproof
                node.proof = min(node.proof, child.proof)
    else:
        if node.value = "WIN":
            node.proof = 1000000
            node.disproof = 0
        elif node.value = "LOSE":
            node.proof = 0
            node.disproof = 1000000
        elif node.value = "UNKNOWN":
            node.proof = 1
            node.disproof = 1

def selectMostProvingNode(node):
    best = 0
    while node.expanded:
        value = 1000000
        if node.type = "AND":
            for child in node.children
                if value > child.disproof:
                    best = child
                    value = child.disproof
        elif node.type = "OR":
            for child in node.children
                if value > child.proof:
                    best = child
                    value = child.proof
    node = best
    return node

def expandNode(node):
    node.children = generateChildren(node)
    for child in node.children:
        evaluate(child)
        setProofAndDisproofNumbers(child)
        if node.type = "AND" :
            if child.disproof is 0:
                return node
        else:
            if child.proof is 0:
                return node

    node.expanded = True
    return node

def updateAncestors(node, root):
    while node is not root:
        oldProof = node.proof
        oldDisproof = node.disproof
        setProofAndDisproofNumbers(node)
        if node.proof is oldProof and node.disproof is oldDisproof:
            return node

        node = node.parent

    setProofAndDisproofNumbers(root)
    return root

def generateChildren(node):
    for i in range(10):
        for j in range(10):
            child = node
            if node.type is "AND":
                child.type = "OR"
            else:
                child.type = "AND"

            child.parent = node

            if player is True:
                board[i][j] = "B"
            else:
                board[i][j] = "R"

            if player is True:
                player = False
            else:
                player = True

            child.board = board
            board[i][j] = 0
            node.children.update(child)


def evaluate(root):
    if checkOfWin is "B":
        return "WIN"
    elif checkOfWin is "R":
        return "LOSE"

    else return None



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
    return None
