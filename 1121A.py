n,m,k=map(int,input().split())
p=[int(o) for o in input().split()]
s=[int(o) for o in input().split()]
maxs=[[-1,i] for  i in range(m+1)]
for i in range(n):
    if maxs[s[i]][0]<p[i]:
        maxs[s[i]][0]=p[i]
        maxs[s[i]][1]=i+1
#print(maxs)
ki=[int(o) for o in input().split()]
lol=0
for i in range(k):
    if maxs[s[ki[i]-1]][1]!=ki[i]:
        lol+=1
print(lol)