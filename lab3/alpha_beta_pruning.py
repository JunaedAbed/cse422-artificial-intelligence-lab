def minimax(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0 :
        return evalutaion
        
    elif maximizingPlayer:
        maxEval = -10000
        for child in position:
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return maxEval
        
    else:
        minEval = +10000
        for child in position:
            eval = minimax(child, depth - 1, alpha, beta, true)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if alpha >= beta:
                break
        return minEval
 
# driver call           
minimax(currentPosition, 3, -10000, +1000, True)            
