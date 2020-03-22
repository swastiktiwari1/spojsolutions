n=int(input())
s=input()
s=list(s)
d=[]
uhoy=(n-11)
for i in range(n):
    if s[i]=="8":
        d.append(i)
pi=0
pj=0
for i in range(uhoy):
    if i%2==0:
        while pi<n:
            if s[pi]!="8" and s[pi]!=-1:
                s[pi]=-1
                pi+=1
                break
            pi+=1
    else:
        while pj<n:
            if s[pj]=="8":
                s[pj]=-1
                pj+=1
                break
            pj+=1
flag=0
#print(s)
for i in range(n):
    if s[i]==-1:
        kmg=0
    elif s[i]=="8":
        break
    else:
        flag=1
        break
if flag==0:
    print("YES")
else:
    print("NO")