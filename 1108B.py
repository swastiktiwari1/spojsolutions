from collections import Counter
n=int(input())
a=[int(o) for o in input().split()]
a=sorted(a)
m=a[-1]
z=[]
z1=dict(Counter(a))
lol=[]
for i in range(len(a)):
    if z1[a[i]]==2:
        lol.append(a[i])
    if m%(a[i])!=0:
        z.append(a[i])
try:
    print(m,z[-1])
except:
    print(m,lol[-1])