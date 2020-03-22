n=int(input())
s=input()
s=list(s)
oc=0
cc=0
occ=s.count("(")
ccc=s.count(")")
flag=0
if n%2!=0:
    flag=1
for i in range(n):
    if s[i]=="(":
        oc+=1
    elif s[i]==")":
        cc+=1
    else:
        if occ<n//2:
            s[i]="("
            oc+=1
            occ+=1
        else:
            s[i]=")"
            cc+=1
            ccc+=1
    if i!=n-1 and cc>=oc:
        flag=1
if oc==cc and flag==0:
    print("".join(s))
else:
    print(":(")