n=int(input())
s=input()
a=[int(o) for o in input().split()]
dp=[[0 for i in range(5)] for j in range(n+1)]
for i in range(n+1):
    dp[i][4]=float('inf')
word=list("hard")
di={"h":0,"a":1,"r":2,"d":3}
for i in range(1,n+1):
    dp[i][0]=dp[i-1][0]
    dp[i][1]=dp[i-1][1]
    dp[i][2]=dp[i-1][2]
    dp[i][3]=dp[i-1][3]
    if s[i-1] in word:
        dp[i][di[s[i-1]]]=min(a[i-1]+dp[i][di[s[i-1]]],dp[i][di[s[i-1]]-1])
print(min(dp[n]))