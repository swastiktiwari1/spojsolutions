from collections import Counter
s=raw_input()
t=[]
u=[]
s=list(s)
cc=dict(Counter(s))
f=sorted(list(set(s)))
ch=f[0]
k=0
for i in range(len(s)):
    t.append(s[i])
    cc[s[i]]-=1
    while cc[ch]==0:
        k+=1
        try:
            ch=f[k]
        except:
            break
    while t[-1]<=ch:
        gg=t.pop()
        u.append(gg)
        if not t:
            break
    #print(s[i],"".join(u),ch)

while t:
    gg=t.pop()
    u.append(gg)
print("".join(u))