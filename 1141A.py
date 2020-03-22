n,m=map(int,input().split())
ans=0
if m%n==0:
    val=m//n
    while val%3==0:
        val//=3
        ans+=1
    while val%2==0:
        val//=2
        ans+=1
    print(ans if val==1 else "-1")
else:print("-1")