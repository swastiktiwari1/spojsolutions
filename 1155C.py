import math
try:
    n,m=map(int,input().split())
    x=[int(o) for o in input().split()]
    x1=x[:]
    x1=sorted(x1)
    y=[int(p) for p in input().split()]
    u=min(x)
    x=list(set(x))
    x=sorted(x)
    mi=0
    n=len(x)
    for i in range(n):
        x[i]=x[i]-u
    ma=x[1]
    for i in range(n-1):
        m=x[i+1]-x[i]
        if m>ma:
            if m%ma==0:
                ma=ma
            else:
                ma=math.gcd(m,ma)
        else:
            if ma%m==0:
                ma=m
            else:
                ma=math.gcd(m,ma)
    flag=0
    for i in range(m):
        if ma%y[i]==0:
            print("YES")
            print(x1[0],i+1)
            flag=1
            break
    if flag==0:
        print("NO")
except:
    print("NO")