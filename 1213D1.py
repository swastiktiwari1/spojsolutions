n,k=map(int,input().split())
a=[int(o) for o in input().split()]
arr=[[] for i in range(200005)]
for i in range(n):
    lol=a[i]
    j=0
    arr[lol].append(j)
    while lol!=0:
        lol//=2
        j+=1
        arr[lol].append(j)

ans=[]
for i in range(200005):
    if len(arr[i])>=k:
        arr[i].sort()
        ans.append(sum(arr[i][:k]))
print(min(ans))