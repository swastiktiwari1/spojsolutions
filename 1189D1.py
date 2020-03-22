import math
n=int(input())
adj=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
if n==2:
    print("YES")
elif n==3:
    print("NO")
else:
    flag=0
    for i in range(n):
        if len(adj[i])==2:
            flag=1
            break
    print("YES" if flag==0 else "NO")