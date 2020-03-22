n=int(input())
lol=[]
d=dict()
d1=dict()
for i in range(n):
    x,y,z=map(int,input().split())
    lol.append([x,y,z,i+1])
lol.sort()
for ii in range(n):
    x=lol[ii][0]
    y=lol[ii][1]
    z=lol[ii][2]
    i=lol[ii][3]-1
    try:
        d[str([x,y])].append(i+1)
    except:
        d[str([x,y])]=[i+1]
    try:
        d1[x].append(i+1)
    except:
        d1[x]=[i+1]
vis=[False]*n
ans=[]
for i in d.values():
    #i.sort()
    if len(i)>=2:
        for j in range(len(i)//2):
            vis[i[j*2]-1]=True
            vis[i[j*2+1]-1]=True
            ans.append([i[j*2],i[j*2+1]])
for i in d1.values():
   # i.sort()
    n1=len(i)
    if n1>=2:
        j=0
        k=1
        while k<n1:
            if vis[i[j]-1]==True:
                j+=1
            if vis[i[k]-1]==True or j==k:
                k+=1
            if k<n1 and vis[i[k]-1]==False and vis[i[j]-1]==False:
                ans.append([i[k],i[j]])
                vis[i[k]-1]=True
                vis[i[j]-1]=True
#lol=sorted(lol)
i=0
j=1
c=0
while j<n:
    if vis[lol[i][3]-1]==True:
        i+=1
    if vis[lol[j][3]-1]==True or j==i:
        j+=1
    if j<n and vis[lol[i][3]-1]==False and vis[lol[j][3]-1]==False:
        ans.append([lol[i][3],lol[j][3]])
        vis[lol[i][3]-1]=True
        vis[lol[j][3]-1]=True
for i in ans:
    print(*i)