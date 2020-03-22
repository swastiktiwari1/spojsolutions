def getv(x):
    x1=1
    if x[-1]==0:
        x.pop()
    #print(x[::-1])
    for i in x:
        x1*=int(i)
    return x1
n=input()
n=list(n)
n=n[::-1]
n1=n[:]
ma=getv(n)
for i in range(len(n)-1):
    n1[i]=9
    n1[i+1]=int(n1[i+1])-1

    ma=max(ma,getv(n1))
print(ma)