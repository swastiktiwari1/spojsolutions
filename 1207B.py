n,m=map(int,input().split())
a=[None]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
b=[[0]*m for i in range(n)]
ans=[]
for i in range(n-1):
    for j in range(m-1):
        if a[i][j]==1 and a[i+1][j+1]==1 and a[i+1][j]==1 and a[i][j+1]==1:
            ans.append([i+1,j+1])
            b[i][j]=1
            b[i+1][j+1]=1
            b[i][j+1]=1
            b[i+1][j]=1
flag=0
for  i in range(n):
    for j in range(m):
        if a[i][j]!=b[i][j]:
            flag=1
            break
    if flag==1:
        break
if flag==1:
    print("-1")
else:
    print(len(ans))
    for i in ans:
        print(*i)