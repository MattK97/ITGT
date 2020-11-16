def abnegamax(board, depth, alpha, beta, sign):
    if depth==0:
        return heuristic() * sign

    bestScore = -np.inf
    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                board[i][j] = "B"
                alpha = max(alpha, -abnegamax(board, depth-1, -beta, -alpha, -sign))
                board[i][j] = 0
                if alpha >= beta:
                    return alpha
    return alpha
