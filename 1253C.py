import math
n,m=map(int,input().split())
a=[int(o) for o in input().split()]
a=sorted(a)
nod=math.ceil(n/m)
s=0
pa=[0]*m
ans=0
for i in range(nod):
    for j in range(m):
        if (m*i+j)<n:
            ans+=a[m*i+j]
            print(ans+pa[j],end=" ")
            pa[j]+=ans