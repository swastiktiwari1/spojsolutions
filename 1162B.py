n,m=map(int,input().split())
m1=[None]*n
m2=[None]*n
for i in range(n):
    m1[i]=[int(o) for o in input().split()]
for i in range(n):
    m2[i]=[int(o) for o in input().split()]
lol=0
for i in range(n):
    for j in range(m):
        if i>0:
            if m1[i][j]<=m1[i-1][j]:
                m1[i][j],m2[i][j]=m2[i][j],m1[i][j]
            if m2[i][j]<=m2[i-1][j]:
                m1[i][j],m2[i][j]=m2[i][j],m1[i][j]
            if m1[i][j]<=m1[i-1][j] or m2[i][j]<=m2[i-1][j]:
                lol=1
                break
        if j>0:
            if m1[i][j]<=m1[i][j-1]:
                m1[i][j],m2[i][j]=m2[i][j],m1[i][j]
            if m2[i][j]<=m2[i][j-1]:
                m1[i][j],m2[i][j]=m2[i][j],m1[i][j]
            if m1[i][j]<=m1[i][j-1] or m2[i][j]<=m2[i][j-1]:
                lol=1
                break
print("Possible" if lol==0 else "Impossible")