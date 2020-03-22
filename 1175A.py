for _ in range(int(input())):
    n,k=map(int,input().split())
    s=0
    while n!=0:
        #print(n,s)
        if n<k:
            s+=(n)
            n=0
            
        elif n%k==0:
            n=n//k
            s+=1
        else:
            s=s+(n%k)+1
            n=n//k
    print(s)