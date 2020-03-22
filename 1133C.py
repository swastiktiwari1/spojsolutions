from collections import Counter
n=int(input())
a=[int(o) for o in input().split()]
b=[int(o) for o in input().split()]
c=[0]*n
for i in range(n):
    try:
        c[i]=-b[i]/a[i]
    except:
        c[i]="lol"
d=dict(Counter(c))
ma=0
for i in d.keys():
    if i!="lol":
        ma=max(d[i],ma)
print(ma)