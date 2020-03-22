import math
n=int(input())
a=[int(o) for o in input().split()]
b=[]
ma=max(a)
for i in range(n):
    if a[i]!=ma:
        b.append(ma-a[i])
if b:
    g=b[0]
    for i in range(1,len(b)):
        g=math.gcd(g,b[i])
    y=0
    for i in b:
        y+=(i//g)
    print(y,g)
else:
    print(0,0)