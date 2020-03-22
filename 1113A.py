n,v=map(int,input().split())
if v>=n-1:
    print(n-1)
else:
    count=v
    c=v
    for i in range(1,n):
        if count>=(n-i):
            break
        if count<v:
            count=v
            c+=i
        count-=1
    print(c)