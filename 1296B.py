for _ in range(int(raw_input())):
    n=int(raw_input())
    c=0
    while n!=0:
        p=(n/10)
        if p!=0:
            c+=(p)*10
            n=p+(n-(p*10))
            # print(n)
        else:
            c+=n
            n=0
    print(c)