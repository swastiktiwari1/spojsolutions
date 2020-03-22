
n=int(input())
c=[0]*n
adj=[[] for i in range(n)]
child=[False]*n
parent=[False]*n
for i in range(n):
    a,b=map(int,input().split())
    if b==0:
        child[i]=True
    if a!=-1:
        parent[a-1]|=child[i]
    else:
        p=i
        c[i]=False
hhk=0
for i in range(n):
    if child[i]==False and parent[i]==False:
        print(i+1,end=" ")
        hhk=1
if hhk==0:
    print("-1")