for _ in range(int(input())):
    n,m=map(int,input().split())
    m1=m
    m2=m1
    s=set()
    while True:
        if int(str(m)[-1]) in s:
            break
        else:
            s.add(int(str(m)[-1]))
            m+=m1
    ls=len(s)
    no=(n//m2)//ls
  #  print(n//m2)
   # print(s)
    ans=(sum(s)*no)
    ff=(n//m2)%ls
    
    for i in range(ff):
        ans+=int(str(m1)[-1]) 
        m1+=m2
    print(ans)