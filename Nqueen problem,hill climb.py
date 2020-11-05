"""
this program works using an array of integers depicting the position of queen in each row, 
instead of using a matrix
EXAMPLE - the chess position-:
                         0 1 0 0
                         0 0 1 0
                         1 0 0 0
                         0 0 0 1
                         
is used in the program as array [1,2,0,3] 
"""

#displays the answer in standard matrix form
def display(visited): 
    for i in range(len(visited)):
        temp=[[0 for y in range(n)] for u in range(n)]
        for j in range(n):
            temp[j][visited[i][j]]=1
            print(temp[j])
        print()

#calculates the positional errors in the given array, 
#the result is used as heuristic, the lower the better
def check(chess): 
    errs=0
    for k in range(n):
        i=chess[k]
        for j in range(0,n):
            if chess[j]!=i or j==k:
                continue
            else:
                #print(1)
                errs+=1
        for j in range(0,n):
            if ((j+i-k<0 or j+i-k>n-1) or chess[j]!=j+i-k)or j==k:
                continue
            else:
                #print(2)
                errs+=1
        for j in range(0,n):
            if ((i+k-j<0 or i+k-j>n-1) or chess[j]!=i+k-j)or j==k:
                continue
            else:
                #print(3)
                errs+=1 
    return int(errs/2)
    
import copy
#this function generates neighbours of a given array by changing only one row of the chessboard
#then the hill climb algorithm is implemented using recursion
def hill_climb(init_chess,visited):
    visited.append(init_chess)
    neighbours=[]
    if(check(init_chess)==0):       #checking if solution found
        print("solution found")
        display(visited)
        return
    for i in range(n):              #generating neighbours (new states)
        for j in range(n):
            temp=copy.deepcopy(init_chess)
            temp[i]=j;
            neighbours.append([check(temp),temp])
    neighbours.sort()               #sorting iterations by heuristic value
    if (neighbours[0][0]<check(init_chess)): #checking if new state is better than current state
        visited=hill_climb(neighbours[0][1],visited)
    else:
        print("solution not reached")
        display(visited)
        return 
    return 
  # driver code
n=4
chess=[1,1,0,1]
hill_climb(chess,[])
