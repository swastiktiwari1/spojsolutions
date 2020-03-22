for _ in range(int(input())):
    n,p,k=map(int,input().split())
    a=[int(o) for o in input().split()]
    p1=p
    taken=[0]*n
    a=sorted(a)
    i=1
    items=0
    res=[]
    while p>0 and i<n:
        if a[i]<=p and taken[i]==0:
            items=(i+1)
            p-=a[i]
            taken[i]=1
            i+=k
            if i>=n:
                i=n-1
        elif a[i-1]<=p and taken[i-1]==0:
            items=i
            p-=a[i-1]
            taken[i-1]=1
            i+=k
            if i>=n:
                i=n-1
        else:
            break
    res.append(items)
    i=0
    taken=[0]*n
    items=0
    p=p1
    while p>0 and i<n:
        if a[i]<=p and taken[i]==0:
            items=(i+1)
            p-=a[i]
            taken[i]=1
            i+=k
            if i>=n:
                i=n-1
        elif i-1>=0 and a[i-1]<=p and taken[i-1]==0:
            items=i
            p-=a[i-1]
            taken[i-1]=1
            
            i+=k
            if i>=n:
                i=n-1
        else:
            break
    # print(res)
    res.append(items)
    # print(res)
    print(max(res))