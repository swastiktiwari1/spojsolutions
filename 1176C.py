n=int(input())
a=[int(o) for o in input().split()]
dp=[[0 for i in range(7)] for j in range(n+1)]
#print(dp[0])
d={4:0,8:1,15:2,16:3,42:5,23:4}
for i in range(n):
    dp[i][0]=dp[i-1][0]
    if a[i]==4:
        dp[i][0]+=1
for i in range(n):
    for j in range(7):
        dp[i][j]=max(dp[i][j],dp[i-1][j])
    if dp[i-1][d[a[i]]-1]!=0:
        dp[i][d[a[i]]]=min(dp[i-1][d[a[i]]]+1,dp[i-1][d[a[i]]-1])

print(n-6*dp[n-1][5])