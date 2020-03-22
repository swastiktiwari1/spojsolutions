n,m=map(int,input().split())
arr=[None]*n
cx=0
for i in range(n):
    arr[i]=[int(o) for o in input().split()]
    cx^=arr[i][0]
ans=[1]*n
if cx!=0:
    print("TAK")
    print(*ans)
else:
    flag=0
    for i in range(n):
        for j in range(1,m):
            if arr[i][j]!=arr[i][0]:
                ans[i]=j+1
                flag=1
                break
        if flag==1:
            break
    if flag==0:
        print("NIE")
    else:
        print("TAK")
        print(*ans)