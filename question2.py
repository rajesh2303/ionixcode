n=int(input("Enter the Number :"))
''' method 1:res=(n**n)+(n**2) it is using power function '''


'''
n=2=>    8
n=3=>    36
n=4=>    272


for 3
3*3*3=27
3*3=9
9+27=36
'''

#method 2
res,ans=1,1
for i in range(n):#power of n 3*3*3 store in res=27
    res*=n
for i in range(2):#power of n 3*3 store in ans=9
    ans*=n
print(res+ans)#res+ans=36
