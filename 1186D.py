import heapq
import math
n=int(input())
a=[None]*n
h=[]
mh=[]
s=0
d=[0]*n
for i in range(n):
    a[i]=float(input())
    if a[i]!=int(a[i]):
        if a[i]<0:
            heapq.heappush(h,[math.floor(a[i])-math.ceil(a[i]),i])
        else:
            heapq.heappush(mh,[math.ceil(a[i])-math.floor(a[i]),i])
    s+=int(a[i])
    d[i]=int(a[i])
if s==0:
    mfff=0
elif s>0:
        
    for i in range(s):
        k=heapq.heappop(h)
        if a[k[1]]<0:
            d[k[1]]=math.floor(a[k[1]])
        else:
            d[k[1]]=math.ceil(a[k[1]])

else:

    for i in range(-s):
        k=heapq.heappop(mh)
        if a[k[1]]<0:
            d[k[1]]=math.floor(a[k[1]])
        else:
            d[k[1]]=math.ceil(a[k[1]])
    
for i in range(n):
    print(int(d[i]))