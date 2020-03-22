for _ in range(int(input())):
    a,b,n=map(int,input().split())
    if (n+1)%3==1:
        print(a)
    elif (n+1)%3==2:
        print(b)
    else:
        print(a^b)