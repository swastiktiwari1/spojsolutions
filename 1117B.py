n,m,k=map(int,input().split())
a=[int(o) for o in input().split()]
a=sorted(a)
a=a[::-1]
lol=m//(k+1)
uu=m%(k+1)
try:
    rt=(k*a[0])+a[1]
    print(lol*rt+uu*a[0])
except:
    print(k*a[0])