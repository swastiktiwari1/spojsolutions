n=int(input())
a=[int(o) for o in input().split()]
if len(list(set(a)))==1:
    print(-1)
else:
    a=sorted(a)
    print(*a)