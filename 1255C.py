n=int(input())
arr=[None]*(n-2)
d=dict()
nearby=dict()
for i in range(n-2):
    arr[i]=list(map(int,input().split()))
    for j in range(3):
        try:
            nearby[arr[i][j]].add(arr[i][(j+1)%3])
        except:
            nearby[arr[i][j]]=set([arr[i][(j+1)%3]])
        try:
            nearby[arr[i][j]].add(arr[i][(j+2)%3])
        except:
            nearby[arr[i][j]]=set([arr[i][(j+2)%3]])
    for j in arr[i]:
        if j in d:
            d[j]+=1
        else:
            d[j]=1
d1=dict()
for i in d:
    try:
        d1[d[i]].add(i)
    except:
        d1[d[i]]=set([i])
ans=[]
last=[]
aagye=set()
j=0
for i in d1[1]:
    if (j%2)==0:
        ans.append(i)
        aagye.add(i)
    else:
        last.append(i)
    j+=1
for i in d1[2]:
    if i in nearby[ans[0]]:
        ans.append(i)
        aagye.add(i)
    else:
        last.append(i)
for i in range(n-4):
    lol=(nearby[ans[-1]]&nearby[ans[-2]])
    for k in lol:
        if k not in aagye:
            ans.append(k)
            aagye.add(k)
print(*ans,*last[::-1])