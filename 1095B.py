n=int(input())
a=[int(n) for n in input().split()]
a=sorted(a)
b=a[:]
c=a[:]
b.pop(0)
c.pop()
print(min(c[-1]-c[0],b[-1]-b[0]))