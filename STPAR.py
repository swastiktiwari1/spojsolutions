while True:
    n=int(input())
    if n==0:
        break
    a=[]
    c=1
    u=[int(o) for o in input().split()]
    flag=0
    i=0
    lu=len(u)
    while c<=n:
        if len(a)>0 and a[-1]==c:
            c+=1
            a.pop()
        elif i<lu and u[i]==c:
            i+=1
            c+=1
        elif i!=n:
            a.append(u[i])
            i+=1
        else:
            flag=1
            break
    
    print("yes" if flag==0 else "no")
            
            
            
