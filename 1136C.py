n,m=map(int,input().split())
a=[None]*n
b=[None]*n
f=[None]*(n+m)
g=[None]*(n+m)
for i in range(n+m):
    f[i]=[]
    g[i]=[]
for i in range(n):
    a[i]=[int(o) for o in input().split()]
    for j in range(m):
        f[i+j].append(a[i][j])
for i in range(n):
    b[i]=[int(o) for o in input().split()]
    for j in range(m):
        g[i+j].append(b[i][j])
flag=0
for i in range(m+n):
    f[i]=sorted(f[i])
    g[i]=sorted(g[i])
    if f[i]!=g[i]:
        flag=1
        break
if flag==0:
    print("YES")
else:
    print("NO")