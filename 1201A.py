from collections import Counter
n,m=map(int,input().split())
d=dict()
for i in range(n):
    s=input()
    for j in range(m):
        try:
            d[j].append(s[j])
        except:
            d[j]=[s[j]]
ans=0
a=[int(o) for o in input().split()]
for i in range(m):
    f=dict(Counter(d[i]))
    m=0
    for j in f.values():
        m=max(m,j)
   # print(m)
    ans+=(m*a[i])
print(ans)