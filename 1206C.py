n=int(input())
if n%2==0:
    print("NO")
elif n==1:
    print("YES")
    print("1 2")
else:
    pi=1
    np1=(n*2)
    ans=[1]
    for i in range(2*n-1):
        if i%2!=0:
            pi=(pi+1)
            if pi>np1:
                pi-=np1
        else:
            pi=(pi+3)
            if pi>np1:
                pi-=np1
        ans.append(pi)
    print("YES")
    #print(len(set(ans)))
    print(*ans)