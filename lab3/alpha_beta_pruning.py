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
        # print('leaf value:', evaluations[_])
    
    return depth, node_num, leaf_nodes_num, evaluations



def minimax(position, depth, alpha, beta, maximizingPlayer, count):
    if depth == 0 :
        return evaluations[position], count + 1
        
    if maximizingPlayer:
        maxEval = -10000
        for child in range(node_num):
            eval, count = minimax((position * node_num) + child, depth - 1, alpha, beta, False, count)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if alpha >= beta:
                count - 1
                break
        return maxEval, count
        
    else:
        
        minEval = 10000
        for child in range(node_num):
            eval, count = minimax((position * node_num) + child, depth - 1, alpha, beta, True, count)
            
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if alpha >= beta:
                count - 1
                break
        return minEval, count


def print_screen():
    print('Depth:', depth)
    print('Branch:', node_num)
    print('Terminal States (Leaf nodes):', leaf_nodes_num)
    print('Maximum amount:', max_amount)
    print('Before Alpha-Beta Pruning:', leaf_nodes_num)
    print('After alpha-beta pruning:', count)
 
 
# driver call       
depth, node_num, leaf_nodes_num, evaluations = read_file('lab3/input.txt')    
max_amount, count = minimax(0, depth, -10000, 10000, True, 0)            
print_screen()
