import math
for i in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    m=math.ceil(a/c)
    n=math.ceil(b/d)
    if(m+n>k):
        print(-1)
    else:
        print(m,n)