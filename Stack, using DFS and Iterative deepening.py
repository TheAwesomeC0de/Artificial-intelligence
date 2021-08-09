import copy as copy
globe=[]
visited=[]
n=1
def generate_iterations(base,goal,n):
    if base==goal:
            visited.append(base)
            #print(visited)
            return 1
    if n==0:
        return 0
    while base not in visited:
        visited.append(base)
        for i in range(3):
            for j in range(3):
                if len(base[i])>0 and i!=j:
                    temp=copy.deepcopy(base)
                    x=temp[i].pop()
                    temp[j].append(x)
                    temp.sort()
                    if temp not in visited:
                        t=generate_iterations(temp,goal,n-1)
                        if t==1:
                            return 1
    return 0
if __name__=="__main__":
    flag=0
    start=[[],['A'],['B','C']]
    goal=[[],[],['A','B','C']]
    while flag==0:
        visited=[]
        if generate_iterations(start,goal,n)==1:
            print("depth=",n)
            flag=1
        else:
            n=n+1
    print(generate_iterations(start,goal,200))     
