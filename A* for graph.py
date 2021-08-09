nvertex= 6
"""
the below dictionary is the dataset used by this program
it stores a list corresponding to each vertex in the following format
    vertex: [h_val,current g_val,[list of adjacent vertices with distances]]
"""
graph = {
          'A':[11,999,[['B',2],['E',3]]],
          'B':[6,999,[['A',2],['C',1],['G',9]]],
          'C':[99,999,[['B',1]]],
          'D':[1,999,[['E',6],['G',1]]],
          'E':[7,999,[['D',6],['A',3]]],
          'G':[0,999,[['B',9],['D',1]]]
        }
import copy
#this function updates the g_val of all neighbouring vertices of the input vertex
def update_gval(node):
    node_gval=graph[node][1]
    temp=copy.deepcopy(graph[node][2])
    n=len(temp)
    for i in range(n):
        og=graph[temp[i][0]][1]
        new_gval=node_gval+temp[i][1]
        if og>new_gval:
            graph[temp[i][0]][1]=new_gval
    return

#main function performing the A* search
def ayystar(goal,start):
    graph[start][1]=0
    current=start
    neighbours=[]  #this list will hold all unvisited adjacent vertices in order of their h_val + g_val
    while(True):
        visited.append(current)
        update_gval(current)
        n=len(graph[current][2])
        for i in range(n):
            temp=[0,'Null']
            temp[1]=graph[current][2][i][0]
            temp[0]=graph[temp[1]][0]+graph[temp[1]][1]
            if temp[1]==goal:
                print("goal found at cost",graph[temp[1]][1])
                print(visited)
                return
            if temp[1] not in visited:
                neighbours.append(temp)
        if len(visited)==nvertex:
            print("not found")
            return
        neighbours.sort()
        current=neighbours[0][1]
        neighbours.pop(0)

#driver code
visited=[]
ayystar('G','A')
