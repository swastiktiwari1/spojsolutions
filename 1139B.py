n=int(input())
a=[int(o) for o in input().split()]
a=a[::-1]
ans=a[0]
pans=a[0]
for i in range(1,n):
    if a[i]<pans:
        ans+=a[i]
        pans=a[i]
    else:
        pans=max(pans-1,0)
        ans+=pans
print(ans)