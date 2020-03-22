q=int(input())
for i in range(q):
    k,n,a,b=map(int,input().split())
    k1=k-n*b
    if k1>0:
        bache=k-(b*n)
        diff=a-b
        lol=bache//diff
        if k-lol*a-(n-lol)*b>0:
            print(min(n,lol))
        else:
            lol-=1
            print(min(n,lol))
    else:
        print("-1")