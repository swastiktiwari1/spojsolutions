# cook your dish here
from collections import Counter
T=int(input())
a=[int(n) for n in input().split()]
b=Counter(a)
c=b.values()
print(max(c))