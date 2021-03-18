import random


def read_file(file):
    fr = open(file, 'r')
    turn = int(fr.readline())
    depth = 2 * turn
    node_num = int(fr.readline())
    leaf_nodes_num = node_num ** depth
    min_range, max_range = fr.readline().split(' ')
    min_range = int(min_range)
    max_range = int(max_range)
    evaluations = []
    for _ in range(leaf_nodes_num):
        i = random.randint(min_range, max_range)
        evaluations.append(i)
    
    return depth, node_num, leaf_nodes_num, evaluations



def minimax(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0 :
        return evaluations[position]
        
    if maximizingPlayer:
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


def print_screen(depth, node_num, leaf_nodes_num):
    print('Depth:', depth)
    print('Branch:', node_num)
    print('Terminal States (Leaf nodes):', leaf_nodes_num)
    print('Before Alpha-Beta Pruning:', leaf_nodes_num)
 
# driver call       
depth, node_num, leaf_nodes_num, evaluations = read_file('lab3/input.txt')    
print_screen(depth, node_num, leaf_nodes_num)
minimax(0, depth, -10000, +10000, True)            
