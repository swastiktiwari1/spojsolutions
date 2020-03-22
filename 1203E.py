n=int(input())
a=[int(o) for o in input().split()]
a=sorted(a)
a=a[::-1]
s=set()
for i in a:
    if i+1 not in s:
        s.add(i+1)
    elif i not in s:
        s.add(i)
    elif i-1 not in s and i-1!=0:
        s.add(i-1)
print(len(s))