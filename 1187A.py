for _ in range(int(input())):
    n,s,t=map(int,input().split())
    x=(s+t-n)
    nos=s-x
    nott=t-x
    nob=x
    print(max(nos,nott)+1)