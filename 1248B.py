n=int(input())
a=[int(o) for o in input().split()]
a=sorted(a)
lol=a[n//2:]
lol1=a[:n//2]
print(sum(lol)**2+sum(lol1)**2)