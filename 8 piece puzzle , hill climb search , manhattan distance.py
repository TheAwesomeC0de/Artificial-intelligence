import sys
import copy
s=[]
q = []
visited = []

def compare(s,g):
    if s==g:
        return(1)
    else:
        return(0)

def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return([i,j])

def up(s,pos):
    i = pos[0]
    j = pos[1]

    if i>0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i-j][j]
        temp[i-j][j] = 0
        return temp
    else :
        return (s)

def down(s,pos):
    i = pos[0]
    j = pos[1]
    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i+1][j]
        temp[i+1][j] = 0
        return (temp)
    else:
        return (s)

def right(s,pos):
    i = pos[0]
    j = pos[1]
    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j+1]
        temp[i][j+1] = 0
        return (temp)
    else:
        return (s)

def left(s,pos):
    i = pos[0]
    j = pos[1]
    if j > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j-1]
        temp[i][j-1] = 0
        return (temp)
    else:
        return (s)
def pos(s,r):
    for i in range(3):
        for j in range(3):
            if s[i][j] == r:
                return([i,j])
            
def distance(lst):
    sum=abs(lst[0][0]-lst[1][0])
    sum+=abs(lst[0][1]-lst[1][1])
    return sum

def heuristic(c,g): #manhattan distance
    n=len(c)
    pair=[]
    for i in range(n):
        for j in range(n):
            temp=c[i][j]
            pair.append([[i,j],pos(g,temp)])
    sum=0
    for i in range(len(pair)):
        sum+=distance(pair[i])
    return sum

def search(s,g):
    curr_state = copy.deepcopy(s)
    h_c=heuristic(curr_state,g)
    if s == g:
        return

    global visited
    while(1):
        visited.append(curr_state)
        pos = find_pos(curr_state)
        new = up(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if heuristic(new,g)<h_c :
                    curr_state=new
                    continue
        new = down(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if heuristic(new,g)<h_c :
                    curr_state=new
                    continue

        new = right(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if heuristic(new,g)<h_c :
                    curr_state=new
                    continue
        new = left(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if heuristic(new,g)<h_c :
                    curr_state=new
                    continue
        print ("not found")
        print(visited)
        return

def main():
    global s
    s = [[1,2,3],[4,0,5],[7,8,6]]
    global g
    g = [[1,2,3],[4,5,6],[7,8,0]]
    global q
    global visited
    search(s,g)

if __name__ == "__main__":
    main()
