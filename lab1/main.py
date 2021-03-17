
def read_file(file):
    fr = open(file, 'r')
    number_of_vertex = int(fr.readline())
    lines = int(fr.readline())
    list1 = [[]] * number_of_vertex
    print(list1)
    
    for i in range(lines):
        line = fr.readline().strip().split(' ')
        print(line)
        # list1[int(line[0])].append(int(line[1])) 
        
        list1[int(line[1])].append(int(line[0])) 
        
    linas_position = int(fr.readline())
    print(list1)
    return list1, linas_position
    
    
def bfs(g, root):
    length = len(g[0])
    color = ['black'] * length
    parent = ['null'] * length
    distance = [0]*length
    
    color[root] = 'white'
    parent[root] = -1
    distance[root] = -1
    
    queue = [root]
    
    while queue:
        vertex = queue.pop()
        for i in g[vertex]:
            if color[i] == 'black':
                color[i] = 'white'
                distance[i]=distance[vertex]+1
                parent[i] = vertex
                queue.append(i)
        color[vertex] = 'red'
    return color, parent, distance
        
def distance_finder(pArray, node):
    count = -1
    
    while node != -1:
        node = pArray[node]
        count += 1
    
    return count    
    
graph, goal_node = read_file('input.txt')

color, parent, distance = bfs(graph, 0)        

print(distance)
print(distance_finder(parent, goal_node))
