s=input()
stack,c,l,ll=[-1],1,0,0
for i in range(len(s)):
    if s[i]=="(":
        stack.append(i)
    else:
        stack.pop()
        if stack:
            k=stack[-1]
            if i-stack[-1]>ll:
                ll=i-stack[-1]
                c=1
            elif i-stack[-1]==ll:
                c+=1
        else:
            stack.append(i)
print(ll,c)