import math
from collections import Counter
n,k=map(int,input().split())
a=[None]*n
for i in range(n):
        a[i]=int(input())
d=dict(Counter(a))
ans=0
leftover=0
for i in d.values():
        ans+=((i//2)*2)
        leftover+=i%2
#print(ans,leftover)
print(ans+math.ceil(leftover/2))