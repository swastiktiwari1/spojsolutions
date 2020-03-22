for _ in range(int(input())):
    n,k=map(int,input().split())
    if n==k:
        print("Alice")
    elif n<k:
        if n%3==0:
            print("Bob")
        else:
            print("Alice")
    elif n==k:
        print("Alice")
    else:
        if k%3==0:
            n%=(k+1)
        elif k%3==1:
            n%=(k-1)
        else:
            n%=(k+1)
        if n==k:
            print("Alice")
        elif n%3==0:
            print("Bob")
        else:
            print("Alice")