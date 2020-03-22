s=input()
stack=[]
s=list(s)
sc=0
ec=0
ls=0
cc=0
lc=-1
ml=-1
for i in range(len(s)):
    if sc==0:
        if s[i]=="[":
            ls+=1
            stack.append("[")
            sc=1
    elif cc==0:
        if s[i]==":":
            ls+=1
            cc+=1
            stack.append(":")
    elif s[i]=="|":
        ls+=1
        stack.append("|")
    elif cc>=1 and s[i]==":":
        cc=2
        lc=ls
    elif s[i]=="]":
        if cc==2:
            ml=max(ml,lc+2)
#print(cc)
#print(stack)
print(ml)