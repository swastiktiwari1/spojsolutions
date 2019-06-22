c=1
while True:
    s=input()
    if s[0]=="-":
        break
    stack=[]
    changes=0
    ls=len(s)
    i=0
    while i<ls:
        if s[i]=="}":
            try:
                if stack[-1]=="{":
                    stack.pop()
                else:
                    stack.append("}")
            except:
                stack.append("}")
        else:
            stack.append("{")
        i+=1
    ans=0
    a=0
    lst=len(stack)
    for i in range(lst):
        a=a+(1 if stack[i]=="{" else -1)
        if a<0:
            ans+=1
            a+=2
        if a>lst-i:
            ans+=1
            a-=2
    print(str(c)+".",ans)
    c+=1
            
    
