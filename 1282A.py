for _ in range(int(input())):
    a,b,c,r=map(int,input().split())
    start=c-r
    end=c+r
    s1=min(a,b)
    s2=max(a,b)
    td=s2-s1
    if s2<=start or s1>=end:
        print(s2-s1)
    elif s1>=start and s2<=end:
        print("0")
    elif s1>=start:
        print(s2-end)
    elif s2<=end:
        print(start-s1)
    else:
        print(s2-s1-(end-start))