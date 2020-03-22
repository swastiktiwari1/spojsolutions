import heapq
n,m,r=map(int,input().split())
a=[int(o) for o in input().split()]
b=[int(o) for o in input().split()]
h=[]
if min(a)>=max(b):
    print(r)
else:
    a=sorted(a)
    i=0
    ts=0
    while i<n and a[i]<=max(b) and r>0:
        ts+=(r//a[i])
        r%=a[i]
        i+=1
    print(ts*max(b)+r)