n=int(input())
a=[int(o) for o in input().split()]
a=a[::-1]
print(min(n-a.index(1),n-a.index(0)))