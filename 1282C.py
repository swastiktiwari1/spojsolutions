for _ in range(int(input())):
    n,t,a,b=map(int,input().split())
    pt=[int(o) for o in input().split()]
    times=[int(o) for o in input().split()]
    d=dict()
    for i in range(n):
        try:
            d[times[i]].append(pt[i])
        except:
            d[times[i]]=[pt[i]]
    times=sorted(list(set(times)))
    # d=dict()
    n1=len(times)
  
    c0=pt.count(0)
    c1=pt.count(1)
    c11=c1
    c00=c0
    ans=[0]
    ct=0
    lol=0
    times.append(float('inf'))
    for i in range(n1):
        # print(times[i],c0,c1)
        c0t=c0
        c1t=c1
        ctt=ct
        # print(c0t,c1t)
        lolt=0
        # print(ctt,t,times[i],lol,lolt)  
        # while c0t>0 and ctt+a<times[i]:
        #     c0t-=1
        #     ctt+=a
        #     lolt+=1
        # while c1t>0 and ctt+b<times[i]:
        #     c1t-=1
        #     ctt+=b
        #     lolt+=1
        trr=times[i]-ctt-1
        if trr>0:
            x=(trr)//a
            if x<=c0t:
                c0t-=x
                trr=0
                ctt+=(x*a)
                lolt+=x
            else:
                ctt+=(c0t*a)
                lolt+=c0t
                trr-=(c0t*a)
                c0t=0
            x=(trr)//b
            if x<=c1t:
                c1t-=x
                trr=0
                ctt+=(x*b)
                lolt+=x
            else:
                ctt+=(c1t*b)
                lolt+=c1t
                trr-=(c1t*b)
                c1t=0
                
        # print(ctt,t,times[i],lol,lolt)   
        if ctt<=t and ctt<times[i]:
            ans.append(lol+lolt)
        for j in d[times[i]]:
            # print("vjv",times[i],c0,c1)
            if j==1:
                ct+=b
                c1-=1
                lol+=1
            else:
                ct+=a
                c0-=1
                lol+=1
    if a*c00+b*c11<=t:
        # print("yey")
        ans.append(n)
    # print(ans)
    print(max(ans))