t=int(input())
while t>0:
    s=input()
    d=[]
    c=[]
    flag=0
    ls=len(s)
    si=0
    for i in range(ls):
        if s[i]!=".":
            if flag!=1:
                si=i
                flag=1
            else:
                flag=0
                ee=i
                d.append(s[si:(ee+1)])
        elif flag==1 and i==(ls-1):
            d.append(s[si:(ls)])
        
    #print(d)
    mb=0
    ma=0
    e=[]
    for i in range(len(d)):
        if d[i][0]=="A" and d[i][-1]=="A":
            ma+=len(d[i])-2
        elif d[i][0]=="B" and d[i][-1]=="B":
            mb+=len(d[i])-2
        elif d[i][-1]==".":
            if d[i][0]=="A":
                ma+=len(d[i])-1
            elif d[i][0]=="B":
                mb+=len(d[i])-1
        else:
            e.append(len(d[i])-2)
    if mb==ma:
        ns=0
        s=s[0]
        for i in range(len(e)):
            ns=ns^e[i]
            
        if ns!=0:
            print("A")
        else:
            print("B")
    elif mb>ma:
        
        print("B")
    else:
        print("A")
    
    t-=1
