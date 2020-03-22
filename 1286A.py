n=int(input())
cou=[n//2,n//2]
if n%2!=0:
    cou[1]+=1
a=[int(o) for o in input().split()]
# print(a)
for i in range(n):
    if a[i]==0:
        a[i]=-1
    else:
        a[i]%=2
        cou[a[i]]-=1
# print(list(range(n)))
# print(a)

curr=0
ps=[]
ans=0
ns=[]
# print(cou)
fl=[]
for i in range(1,n):
    if a[i]!=-1:
        if a[i]!=a[curr]:
            if a[curr]==-1:
                fl.append([i,a[i],curr-1,i-1])
            else:
                ns.append([i-curr-1,a[i],curr,i-1])
        else:
            ps.append([i-curr-1,a[i],curr,i-1])
        curr=i
if a[n-1]==-1:
    fl.append([n-1-curr,a[curr],curr+1,n])
ps.sort()
ns.sort()
fl.sort()
# print(ps)
# print(ns)
flag=0
for i in ps:
    # print(cou,i)
    if flag==1 or i[0]<=cou[i[1]]:
    
        for j in range(i[3],i[2],-1):
            if cou[i[1]]>0:
                cou[i[1]]-=1
                a[j]=i[1]
            else:
                cou[(i[1]+1)%2]-=1
                a[j]=(i[1]+1)%2
    else:
        for k in fl:
            if k[3]==n:
                for j in range(k[2],k[3]):
                    if cou[k[1]]>0:
                        cou[k[1]]-=1
                        a[j]=k[1]
                    else:
                        cou[(k[1]+1)%2]-=1
                        a[j]=(k[1]+1)%2
            else:
                for j in range(k[3],k[2],-1):
                    if cou[k[1]]>0:
                        cou[k[1]]-=1
                        a[j]=k[1]
                    else:
                        cou[(k[1]+1)%2]-=1
                        a[j]=(k[1]+1)%2
        for j in range(i[3],i[2],-1):
            if cou[i[1]]>0:
                cou[i[1]]-=1
                a[j]=i[1]
            else:
                cou[(i[1]+1)%2]-=1
                a[j]=(i[1]+1)%2
        flag=1
# print(cou)
if fl and flag==0:
    if 1:

            
        for k in fl:
            # print(k,cou)
            if k[3]==n:
                for j in range(k[2],k[3]):
                    if cou[k[1]]>0:
                        cou[k[1]]-=1
                        a[j]=k[1]
                    else:
                        cou[(k[1]+1)%2]-=1
                        a[j]=(k[1]+1)%2
            else:
                
                for j in range(k[3],k[2],-1):
                    if cou[k[1]]>0:
                        cou[k[1]]-=1
                        a[j]=k[1]
                    else:
                        cou[(k[1]+1)%2]-=1
                        a[j]=(k[1]+1)%2
    
        
for i in ns:
    # print(i,cou)
    
    for j in range(i[3],i[2],-1):
        if cou[i[1]]>0:
            cou[i[1]]-=1
            a[j]=i[1]
        else:
            cou[(i[1]+1)%2]-=1
            a[j]=(i[1]+1)%2
if a[0]==-1 and len(a)>1:
    a[0]=a[1]
ans=0
# print(a)
for i in range(1,n):
    if a[i]!=a[i-1]:
        ans+=1
print(ans)