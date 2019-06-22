while True:
    s=input()
    if s=="0":
        break
    ls=len(s)
    d=[0]*ls
    d[0]=1
    if ls>=2:
        if s[1]!="0":
            d[1]=1
        #print(d)
        #print(s[:2])
        if int(s[:2])<=26 and int(s[:2])>=10:
            d[1]+=1
   # print(d)
    for i in range(2,ls):
       # print(d[i])
        if s[i]!="0":
            d[i]=d[i-1]
        #print(d)
        if int(s[i-1:i+1])<=26 and int(s[i-1:i+1])>=10:
            #print(s[i-1:i+1])
            d[i]+=d[i-2]
        #print(d)
    print(d[-1])
             
