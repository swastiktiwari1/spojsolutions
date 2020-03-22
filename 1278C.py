for _ in range(int(input())):
    
    n=int(input())
    a=[int(o) for o in input().split()]
    for i in range(2*n):
        if(a[i]==2):
            a[i]=-1
    
    pre=[0]*(2*n+2)
    for i in range(1,2*n+1):
        pre[i]=pre[i-1]+a[i-1]
    d=dict()
    for i in range(0,n+1):
        if (pre[n+i]-pre[n]) not in d:
            d[(pre[n+i]-pre[n])]=i
   # print(pre)
   # print(d)
    ans=[]
    for i in range(0,n+1):
        lol=pre[2*n]-(pre[n]-pre[n-i])
     #   print(i,lol)
        if lol in d:
            ans.append(i+d[lol])
    print(min(ans))