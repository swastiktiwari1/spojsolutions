n,c=map(int,input().split())
a=[int(o) for o in input().split()]
b=[int(o) for o in input().split()]
dp=[[0,0] for i in range(n)]
dp[0][1]=c
print("0",end=" ")
for i in range(1,n):
    dp[i][0]=min(dp[i-1][0]+a[i-1],dp[i-1][1]+a[i-1])
    dp[i][1]=min(dp[i-1][1]+b[i-1],dp[i-1][0]+b[i-1]+c)
    print(min(dp[i]),end=" ")
print()