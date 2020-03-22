s=input()
t=input()
t=list(t)
s=list(s)
ls=len(s)
lt=len(t)
flag=0
if ls !=lt:
    print("No")

else:
    for i in range(ls):
        if s[i]=="a" or s[i]=="e" or s[i]=="i"  or s[i]=="o" or s[i]=="u":
            if t[i]=="a" or t[i]=="e" or t[i]=="i"  or t[i]=="o" or t[i]=="u":
                dhfgg=3
            else:
                flag=1
                break
        elif t[i]=="a" or t[i]=="e" or t[i]=="i"  or t[i]=="o" or t[i]=="u":
            if s[i]=="a" or s[i]=="e" or s[i]=="i"  or s[i]=="o" or s[i]=="u":
                fh=98
            else:
                flag=1
                break
    if flag==1:
        print("No")
    else:
        print("Yes")