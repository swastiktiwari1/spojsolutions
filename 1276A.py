for _ in range(int(input())):
    s=input()
    n=len(s)
    ct=0
    co=0
    two=set()
    one=set()
    for i in range(n-2):
        if s[i]=="o" and s[i+1]=="n" and s[i+2]=="e":
            if i-1>=0 and i-2>=0 and s[i-2]=="t" and s[i-1]=="w":
                one.add(i+1)
            else:
                one.add(i+2)
            
        elif s[i]=="t" and s[i+1]=="w" and s[i+2]=="o":
            if i+3<n and i+4<n and s[i+3]=="n" and s[i+4]=="e":
                two.add(i+3)
            else:
                two.add(i+2)
    k=one|two
    print(len(k))
    k=sorted(list(k))
    print(*k)