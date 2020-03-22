a,b,c=map(int,input().split())
if a==b:
    print(a+b+2*c)
else:
    print(2*min(a,b)+2*c+1)