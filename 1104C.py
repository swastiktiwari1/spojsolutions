s=input()
s=list(s)
arr=[[0 for i in range(4)]for j in range(4)]
ls=len(s)
v=0
h=0
for i in range(len(s)):
    if s[i]=="0":
        if v%2==0:
            print("1 1")
            v+=1
        else:
            print("3 1")
            v+=1
    else:
        if h%4==0:
            print("1 3")
            h+=1
        elif h%4==1:
            print("2 3")
            h+=1
        elif h%4==2:
            print("3 3")
            h+=1
        elif h%4==3:
            print("4 3")
            h+=1