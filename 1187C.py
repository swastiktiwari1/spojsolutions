n,m=map(int,input().split())
p=[]
ne=[]
#print(n)
ra=[0]*n
for i in range(m):
    a=[int(o) for o in input().split()]
    if a[0]==1:
        p.append([a[1],a[2]])
    else:
        ne.append([a[1],a[2]])
        for i in range(a[1],a[2]):
            ra[i]=-1
#print(ra)
for i in p:
    for j in range(i[0],i[1]):
        ra[j]=1
flag=0
for i in ne:
    if ra[i[0]:i[1]].count(-1)==0:
        flag=1
        break
if flag==1:
    print("NO")
else:
    print("YES")
    ra[0]=9999
    for i in range(1,n):
        ra[i]=ra[i-1]+ra[i]
    print(*ra)