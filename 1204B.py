n,l,r=map(int,input().split())
x=1
mins=1
for i in range(l-1):
    x*=2
    mins+=x
mins+=(n-l)
x=1
maxs=1
for i in range(r-1):
    x*=2
    maxs+=x
maxs+=(x)*(n-r)
print(mins,maxs)