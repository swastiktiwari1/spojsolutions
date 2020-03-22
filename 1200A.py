n=int(input())
s=str(input())
l=[0]*10
for i in s:
    if i=="L":
        for j in range(10):
            if l[j]!=1:
                l[j]=1
                break
    elif i=="R":
        for j in range(9,-1,-1):
           # print(j)
            if l[j]!=1:
                l[j]=1
                break
    else:
        l[int(i)]=0
for i in l:
    print(i,end="")