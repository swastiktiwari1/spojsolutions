s=input()
ls=len(s)
k=[None]*ls
for i in range(ls):
    if i%2==0:
        k[i]=(1 if s[i]=="-" else 0)
    else:
        k[i]=(0 if s[i]=="-" else 1)
stack=[]
i=0
while i<ls:
    if stack:
        if k[i]!=stack[-1]:
            stack.pop()
        else:
            stack.append(k[i])
    else:
        stack.append(k[i])
    i+=1
print("No" if stack else "Yes")