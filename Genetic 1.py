def crossover(popin):
    n=len(popin)
    popout=[]
    for i in range(n):
        for j in range(i+1,n):
            temp2=[0,0,0,0]
            temp2[0],temp2[1]=popin[i][0],popin[i][1]
            temp2[2],temp2[3]=popin[j][2],popin[j][3]
            popout.append(temp2)
            temp2=[0,0,0,0]
            temp2[0],temp2[1]=popin[j][0],popin[j][1]
            temp2[2],temp2[3]=popin[i][2],popin[i][3]
            popout.append(temp2)
    return popout
  
import copy 
def mutation(popin,ln):
    popout=[]
    for i in range(0,ln):
        for j in range(len(popin)):
            temp=copy.deepcopy(popin[j])
            if (temp[i]==0):
                temp[i]=1
            else:
                temp[i]=0
            popout.append(temp)
    return popout
  
 def check_viability(arr,setin,wmax):
    wnod=0
    for i in range(len(setin)):
        if setin[i]==1:
            wnod+=arr[i]
    if wnod<=wmax:
        return wnod
    else:
        return False

#driving code:
initialpop=[[1,1,1,0],[1,0,0,1],[0,1,1,1],[1,1,0,1]]
warray=[1,3,5,6]
wmax=10
ln=4
iterations=10
nextcase=[]
testcase=mutation(crossover(initialpop),ln)
for i in range(iterations):
    nextcase=[]
    for i in range(len(testcase)):
        if check_viability(warray,testcase[i],wmax):
            if testcase[i] not in nextcase:
                nextcase.append(testcase[i])
    testcase=copy.deepcopy(nextcase)
print(testcase)
