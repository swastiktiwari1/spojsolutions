n,k=map(int,input().split())
counts=[0]*26
s=input()
i=0
j=k
d=dict()
for i in range(n):
    if s[i] in d:
        d[s[i]].append(i)
    else:
        d[s[i]]=[i]
ss=[]
for i in d.values():
    li=len(i)
    j=0
    ff=0
    while j<n:
        if j+k-1<li:
            if i[j+k-1]-i[j]==k-1:
                ff+=1
                j+=k
            else:
                j+=1
        else:
            break
    ss.append(ff)
print(max(ss))