for _ in range(1):
    n=int(input())
    s=input()
    t=input()
    s=list(s)
    t=list(t)
    if len(s)==len(set(s)) and len(t)==len(set(t)):
        lol=["abc","acb","bac","bca","cab","cba"]
        flag=-1
        i=0
        while i<6:
            if (lol[i][0]==s[0] and lol[i][1]==s[1]) or (lol[i][0]==t[0] and lol[i][1]==t[1]):
                i+=1
            elif  (lol[i][1]==s[0] and lol[i][2]==s[1]) or (lol[i][1]==t[0] and lol[i][2]==t[1]):
                i+=1
            else:
                flag=i
                break
        if flag==-1:
            print("NO")
        else:
            print("YES")
            print(lol[flag][0]*n+lol[flag][1]*n+lol[flag][2]*n)
    else:
        st="abc"*n
        st=list(st)
    
        while True:
            for i in range(3*n-1):
                if (st[i]==s[0] and st[i+1]==s[1]) or (st[i]==t[0] and st[i+1]==t[1]):
                    st[i],st[i+1]=st[i+1],st[i]
    
            flag=0
            for i in range(3*n-1):
                if (st[i]==s[0] and st[i+1]==s[1]) or (st[i]==t[0] and st[i+1]==t[1]):
                    flag=1
            if flag==0:
                break
        if flag==0:
            print("YES")
            print("".join(st))
        else:
            print("NO")