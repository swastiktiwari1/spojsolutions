n=int(input())
a=[int(o) for o in input().split()]
for i in range(n):
    a[i]=min(a[i],-a[i]-1)
if n%2==1:
    x=a.index(min(a))
    a[x]=-a[x]-1
print(*a)