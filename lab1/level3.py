import numpy as np


def read_file(file):
    fr = open(file, 'r')
    number_of_vertex = int(fr.readline())
    lines = int(fr.readline())
    matrix = np.zeros((number_of_vertex, number_of_vertex), dtype='int')

    for i in range(lines):
        line = fr.readline().split()
        matrix[int(line[1])][int(line[0])]=1

    lina_position = int(fr.readline().strip())

    connections = []
    number_of_connections = fr.readline().strip()
    
    while fr.readable() and len(number_of_connections)!=0 :
        connections.append(int(number_of_connections))
        number_of_connections = fr.readline().strip()


    return matrix, lina_position, connections


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
    
       




matrix, lina_position, connections = read_file("input3.txt")
color,parent=bfs(matrix,lina_position)

minimum_move=len(matrix)

while connections:
    minimum_move = min(minimum_move,distance_finder(parent, connections.pop()))

print(minimum_move)
