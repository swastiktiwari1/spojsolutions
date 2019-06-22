for _ in range(int(input())):
    s=input()
    s=list(s)
    s1=[]
    s2=[]
    b=["+", "-", "*", "/", "^" ,"(",")"]
    for i in range(len(s)):
        if s[i] in b:
            s1.append(s[i])
        else:
            s2.append(s[i])
        if len(s1)>0 and s1[-1]==")":
            s1.pop()
            s2.append(s1.pop())
            s1.pop()
    print("".join(s2))
