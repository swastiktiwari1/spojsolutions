q=int(input())
for i in range(q):
    n,k=map(int,input().split())
    a=[int(o) for o in input().split()]
    b=min(a)+k
    flag=0
    for i in range(n):
        if abs(a[i]-b)>k:
            flag=1
            break
    print(b if flag==0 else "-1")