n,m = list(map(int,input().split()))
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
s=0
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if a[i][j]==0:
            l = min(a[i+1][j]-1,a[i][j+1]-1)
            a[i][j]=l
        s+=a[i][j]
for i in range(n):
    for j in range(m-1):
        if a[i][j]>=a[i][j+1]:
            print(-1)
            exit()
for i in range(n-1):
    for j in range(m):
        if a[i][j]>=a[i+1][j]:
            print(-1)
            exit()
print(s)