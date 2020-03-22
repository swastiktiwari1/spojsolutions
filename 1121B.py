n=int(input())
a=[int(o) for o in input().split()]
a=sorted(a)
d=dict()
for i in range(n-1):
    for j in range(i+1,n):
        try:
            d[a[i]+a[j]]+=1
        except:
            d[a[i]+a[j]]=1
f=1
for i in d.values():
    f=max(f,i)
print(f)