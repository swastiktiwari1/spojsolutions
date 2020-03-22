n,k,m=map(int,raw_input().split())
a=list(map(int,raw_input().split()))
a=sorted(a)
s=sum(a)
le=len(a)
best=1.0*s/le
for i in range(min(m+1,len(a))):
    add=min(m-i,k*le)
    best=max((s+add)*1.0/le,best)
    s-=a[i]
    le-=1
print best