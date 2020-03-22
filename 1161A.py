n,k=map(int,input().split())
res=0
a=[int(o) for o in input().split()]
first=[9999999 for i in range(n)]
last=[-1 for i in range(n)]
ans=0
for i in range(k):
    if first[a[i]-1]==9999999:
        first[a[i]-1]=i
    last[a[i]-1]=i
for i in range(n):
    if first[i]>last[i]:
        ans+=1
    if i!=n-1:
        if first[i]>last[i+1]:
            ans+=1
    if i!=0:
        if first[i]>last[i-1]:
            ans+=1
print(ans)