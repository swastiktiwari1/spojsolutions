for _ in range(int(input())):
    n=int(input())
    a=[int(o) for o in input().split()]
    s=0
    cnt=0
    o,t=0,0
    for i in range(n):
        if a[i]%3==0:
            cnt+=1
        elif a[i]%3==1:
            o+=1
        elif a[i]%3==2:
            t+=1
            
    u=min(o,t)
    cnt+=u
    o-=u
    t-=u
    cnt=cnt+o//3+t//3
    print(cnt)