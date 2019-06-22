try:
    s=input()
    m=[]
    flag=0
    for i in range(len(s)):
        if s[i]=="C":
            m.append(12)
        elif s[i]=="O":
    
            m.append(16)
        elif s[i]=="H":
            m.append(1)
        elif s[i]=="(":
            m.append("(")
        elif s[i]==")":
            sdd=0
            while m[-1]!="(":
                sdd+=m.pop()
            m.pop()
            m.append(sdd)
        elif s[i]>='2' and s[i]<='9':
            m.append(m.pop()*int(s[i]))
    gg=0
    while True:
        try:
            gg+=m.pop()
        except:
            break
        
    print(gg)
except:
    print("0")
                    
                
    
