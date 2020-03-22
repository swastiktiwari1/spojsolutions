s=input()
s=list(s)
found=0
ls=len(s)
mark=[0]*ls
i=0
stack=[]
ssl=0
for i in s:
    stack.append(i)
    ssl+=1
    while ssl>=2:
        if stack[-1]==stack[-2]:
            found+=1
            stack.pop()
            stack.pop()
            ssl-=2
        else:
            break
#print(found)
if found%2==0:
    print("No")
else:
    print("Yes")