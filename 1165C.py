n=int(raw_input())
s=raw_input()
a=list(s)
stack=[]
sc=0
an=0
for i in range(n):
    if sc%2!=0:
        if stack[-1]==a[i]:
            an+=1
        else:
            stack.append(a[i])
            sc+=1
    else:
        stack.append(a[i])
        sc+=1
if sc!=2*(len(stack)/2):
    sc-=1
    an+=1
    stack.pop()
print(an)
print("".join(stack))