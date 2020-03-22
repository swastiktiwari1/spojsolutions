n=int(input())
a=[None]*3
a[0]=[int(o) for o in input().split()]
a[1]=[int(o) for o in input().split()]
a[2]=[0 for i in range(n)]
dp=[[-float('inf') for i in range(3)]for j in range(n+1)]
for i in range(n):
        for j in range(3):
                dp[i+1][j]=max(dp[i][j-1]+a[j][i],dp[i][j-2]+a[j][i],a[j][i])
print(max(dp[n]))