for _ in range(int(input())):
    n=int(input())
    u=[o for o in input().split()]
    i=n-2
    flag=0
    while i>=0:
        if u[i]<u[i+1]:
            flag+=1
            break
        
        i-=1
    j=n-1
    while j>0:
        if u[j]>u[i]:
            flag+=1
            break
        else:
            j-=1
    u[j],u[i]=u[i],u[j]
    
    u=u[:i+1]+(u[(i+1):][::-1])
    if flag==2:
        print("".join(u))
    else:
        print("-1")
