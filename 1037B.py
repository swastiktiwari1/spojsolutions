n,m=map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a)
s=0
for i in range(n):
    if i<n//2:
        s+=max(0,a[i]-m)
    elif i==n//2:
        s+=abs(m-a[i])
    else:
        s+=max(0,m-a[i])
print(s)