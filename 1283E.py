n=int(input())
a=[int(o) for o in input().split()]
a=sorted(a)
s=set()
for i in range(n):
    if a[i]-1 in s:
        s.add(a[i]-1)
    elif a[i] in s:
        s.add(a[i])
    else:
        s.add(a[i]+1)
mi=len(s)
s=set()
for i in range(n):
    if a[i]-1 not in s:
        s.add(a[i]-1)
    elif a[i] not in s:
        s.add(a[i])
    else:
        s.add(a[i]+1)
print(mi,len(s))