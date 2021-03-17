
import numpy as np


def read_file(file):
    fr = open(file, 'r')
    number_of_vertex = int(fr.readline())
    lines = int(fr.readline())
    matrix = np.zeros((number_of_vertex, number_of_vertex), dtype='int')
    
    for i in range(lines):
        line = fr.readline().split(' ')
        matrix[int(line[0])][int(line[1])] = 1
        matrix[int(line[1])][int(line[0])] = 1
        
    linas_position = int(fr.readline())
    nora_position = int(fr.readline())
    lara_position = int(fr.readline())
    
    return matrix, linas_position, nora_position, lara_position
 
    
        
def bfs(g, root):
    length = len(g[0])
    parent = ['null'] * length
    color = ['black'] * length
    
    
    parent[root] = -1
    color[root] = 'white'
    
    
    queue = [root]
    
    while queue:
        vertex = queue.pop()
        for i in range(len(g[vertex])):
            if g[vertex][i] == 1 and color[i] == 'black':
                parent[i] = vertex
                color[i] = 'white'
                queue.append(i)
        color[vertex] = 'red'
    return color, parent
    
def distance_finder(pArray, node):
    count = -1
    
    while node != -1:
        node = pArray[node]
        count += 1
    
    return count    
    
graph, goal_node, lara_position, nora_position = read_file('input2.txt')

color, parent = bfs(graph, 0)        

if distance_finder(parent, lara_position) < distance_finder(parent, nora_position):
    print('lara')
else: 
    print('nora')    
 