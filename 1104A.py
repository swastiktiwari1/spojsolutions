n=int(input())
i=max(min(9,n-1),1)
while i>=1:
    if n%i==0:
        print(n//i)
        a=[i for j in range((n//i))]
        print(*a)
        break
    i-=1