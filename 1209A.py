n=int(input())
l=list(map(int,input().split()))
t=[]
ans=0
l.sort()
for i in range(n):
    if l[i] not in t:
        t.append(l[i])
        for j in range(i+1,n):
            if l[j]%l[i]==0:
                t.append(l[j])
        ans+=1
    else:
        pass
print(ans)