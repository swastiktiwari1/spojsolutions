from collections import Counter
n=int(input())
a=[int(o) for o in input().split()]
d=dict(Counter(a))
j=0
reserve=[]
resul=[-1]*n
for i in range(n):
    if d[a[i]]==1:
        if j%2==0:
            resul[i]="A"
        else:
            resul[i]="B"
        j+=1
    elif d[a[i]]>2:
        resul[i]="A"
        reserve.append(i)
    else:
        resul[i]="A"
if j%2==0:
    print("YES")
    print("".join(resul))
else:
    if reserve:
        resul[reserve[0]]="B"
        print("YES")
        print("".join(resul))
    else:
        print("NO")