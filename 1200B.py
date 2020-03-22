for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=[int(o) for o in input().split()]
    a=a[:]
    cb=m
    i=0
    flag=0
    while i<n-1:

        cb+=a[i]
       # print(cb,a[i+1])
        a[i]=0
        if cb>=max(a[i+1]-k,0):
            cb-=max(a[i+1]-k,0)
            i+=1
        else:
            flag=1
            break
    print("YES" if flag==0 else "NO")