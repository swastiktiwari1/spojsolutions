s=input()
n=len(s)
l=[[0, 0] for i in range(n+1)]
flag=0
for i in range(len(s)-1):
    l[i+2][0]=l[i+1][0]
    l[i+2][1]=l[i+1][1]
    if s[i:i+2]=="AB":
        l[i+2][0]=l[i+2][0]+1
        if l[i][1]>=1:
            flag=1
            break
    elif s[i:i+2]=="BA":
        l[i+2][1]=l[i+2][1]+1
        if l[i][0]>=1:
            flag=1
            break
#print(l)
print("YES" if flag==1 else "NO")