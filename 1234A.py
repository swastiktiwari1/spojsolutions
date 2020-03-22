import math
for _ in range(int(input())):
    n=int(input())
    a=[int(o) for o in input().split()]
    s=sum(a)
    print(int(math.ceil(s/n)))