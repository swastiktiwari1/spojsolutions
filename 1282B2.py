for _ in range(int(input())):
    n,p,k=map(int,input().split())
    a=[int(o) for o in input().split()]
    p1=p
    taken=[0]*n
    a=sorted(a)
    dp=[0]*(n+1)
    a.append(0)
    lol=0
    for i in range(n):
        dp[i]=a[i]+dp[i-1]
    cost=dp[:]
    for i in range(k-1,n):
        cost[i]=cost[i-k]+a[i]
    i=n-1
    while cost[i]>p:
        i-=1
    lol=i+1
    #print(cost)
    print(lol)