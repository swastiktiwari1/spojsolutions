def f(x):
    
    for i in range(n-x+1):
        j=[]
        for k in range(i):

            j.append(a[k])
        for k in range(i+x,n):
            j.append(a[k])
       # print(x,j)
        if len(set(j))==len(j):
            return True
    return False
n=int(input())
a=[int(o) for o in input().split()]
s=set()
low=0
high=n
while low<=high:
    mid=(high+low)//2
    #print(mid)
    if f(mid):
        high=mid-1
    else:
        low=mid+1
print(max(low,0))