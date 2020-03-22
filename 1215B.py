n=int(input())
a=[int(o) for o in input().split()]
bal=0
e=0
o=0
ans=0
for i in range(n):

    
    if bal%2==0:
        e+=1
    else:
        o+=1
    if a[i]<0:
        bal+=1
    if bal%2!=0:
        ans+=e
    elif bal%2==0:
       # ans+=1
        ans+=o
    #print(a[i],ans,e,o,bal)
print(ans,(n*(n+1)//2)-ans)