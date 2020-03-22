for _ in range(int(raw_input())):
    n=int(raw_input())
    a=[int(o) for o in raw_input().split()]
    s=set()
    for i in range(n):
        a[i]%=2
        s.add(a[i])
    if len(s)==2:
        print("YES")
    if len(s)==1:
        if n%2==0:
            print("NO")
        else:
            if a[0]==1:
                print("YES")
            else:
                print("NO")