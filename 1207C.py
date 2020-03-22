for _ in range(int(input())):
    n,a,b=map(int,input().split())
    s=input()
    next1=[float('inf')]*(n+1)
    j=float('inf')
    for i in range(n-1,-1,-1):
        next1[i]=j
        if s[i]=='1':
            j=i
    ans=(a*n)+(b*(n+1))
    i=0
    flag=0
   # print(ans)
    while i<n:
        if s[i]=='1':
            if flag==0:
                ans+=a
            ans+=b

            ans+=min((next1[i]-i-1)*b,2*a+b)
            flag=1
            i=next1[i]
           # print(ans)
        else:
            i+=1
    if flag==1:
        ans-=a
    print(ans)