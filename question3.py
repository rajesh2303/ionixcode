'''minimum of cost and distance'''
def find(cost,km,i,c,d,vi,n):
    if i==n-1:  #destination reached
        return (c,d)
    mi=(9999999999,9999999999)
    for j in range(n):
        if km[i][j]>0 and vi[j]==0: #not visited and exsistant path
            vi[j]=1
            res=find(cost,km,j,c+cost[i][j],d+km[i][j],vi,n)
            if sum(mi)>sum(res): #finding minimum cost and distance
                mi=res
            vi[j]=0
    return mi
n=4
cost,km,vi,li=[],[],[],[]
for i in range(n):   
    for j in range(n):
        li.append(0)
    cost.append(li)   #cost matrix
    li=[]
for i in range(n):
    for j in range(n):
        li.append(0)
    km.append(li)   #km matrix
    li=[]
for i in range(n):
    vi.append(0)    #visited matrix
m=int(input("Enter Number of vertices : "))
print("Enter vertices1 vertices2 cost km")
for i in range(m):
    x=input().split()
    cost[ord(x[0])-65][ord(x[1])-65]=int(x[2])
    km[ord(x[0])-65][ord(x[1])-65]=int(x[3])
res=find(cost,km,0,0,0,vi,n)
print("Minimum cost :{}\nMinimum km :{}".format(res[0],res[1]))   #print the km and cost
