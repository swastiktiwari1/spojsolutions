def f(khaya):
    return (((n-khaya)*(1+n-khaya))//2)-khaya-k
n,k=map(int,input().split())
low=0
high=n
i=0
while True:
    i+=1
    mid=(high+low)//2
    #print(mid,f(mid))
    ll=f(mid)
    if ll==0:
        break
    if ll>0:
        low=mid+1
    else:
        high=mid-1
print(mid)