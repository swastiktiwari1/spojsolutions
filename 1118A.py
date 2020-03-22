q=int(input())
while q>0:
    n,a,b=map(int,input().split())
    if b<2*a:
        print((n//2)*b+(n%2)*a)
    else:
        print(n*a)
    q-=1