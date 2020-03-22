from collections import Counter
d=[]
n,m=map(int,input().split())
x1,x2=map(int,input().split())
nx1=[]
nx2=[]
nx1c,nx2c=0,0
for i in range(m-1):
    lol=list(map(int,input().split()))
    if x1 not in lol:
        nx1.extend(list(set(lol)))
        nx1c+=1
    if x2 not in lol:
        nx2.extend(list(set(lol)))
        nx2c+=1
if len(nx1)==0 or len(nx2)==0:
    print("YES")
else:
    flag=0
    cx1=dict(Counter(nx1))
    cx2=(dict(Counter(nx2)))
    for u in cx1.values():
        if u==nx1c:
            flag=1
    for u in cx2.values():
        if u==nx2c:
            flag=1
    print("YES" if flag==1 else "NO")