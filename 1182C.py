
n=int(input())
a=[None]*n
d=dict()
vov=list("aeiou")
for i in range(n):
    a[i]=input()
    vc=0
    lv="a"
    for j in a[i]:
        if j in vov:
            vc+=1
            lv=j
    try:
        d[vc][lv].append(a[i])
    except:
        d[vc]={'a': [],'e': [],'i': [],'o': [],'u': []}
        d[vc][lv].append(a[i])
ans=[[-1 for i in range(4)]for j in range(n)]
si=0
fi=0
for i in d.values():
    if fi!=int(fi):
        fi-=0.5
    for j in i.values():
        for k in range(len(j)//2):
            ans[si][1]=j[2*k]
            ans[si][3]=j[2*k+1]
            si+=1
        for k in range((len(j)//2)*2,len(j)):
            if int(fi)==fi:
                ans[int(fi)][0]=j[k]
            else:
                ans[int(fi)][2]=j[k]
            fi+=0.5
#print(ans)
fa=[]
icans=[]
for i in range(len(ans)):
    if ans[i].count(-1)==0:
        fa.append(ans[i][:])
    elif ans[i][1]!=-1 and ans[i][3]!=-1:
        icans.append([ans[i][1],ans[i][3]])
print(len(fa)+len(icans)//2)
for i in range(len(fa)):
    print(fa[i][0],fa[i][1])
    print(fa[i][2],fa[i][3])
for i in range(len(icans)//2):
    print(icans[i*2][0],icans[i*2+1][0])
    print(icans[i*2][1],icans[i*2+1][1])