n,q=map(int,input().split())
a=[int(o) for o in input().split()]
ma=max(a)
u=a.index(max(a))

qa=[-1]*q

qid=0
ng=[0]*ma

for i in range(u):
    ng[i]=([a[0],a[1]])
    if a[0]>a[1]:
        k=a.pop(1)
        a.append(k)
    else:
        k=a.pop(0)
        a.append(k)
arr=[0]*(n-1)

for i in range(1,n):
    arr[i-1]=a[i]
#print(arr)
for i in range(q):
    que=int(input())
    if que<=ma:
        print(*ng[que-1])
    else:
        print(a[0],arr[(que-ma-1)%(n-1)])