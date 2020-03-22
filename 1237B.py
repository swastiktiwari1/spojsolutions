n=int(input())
a=[int(o) for o in input().split()]
b=[int(o) for o in input().split()]
i=0
j=0
s=set()
ans=0
while i<n and j<n:
    while i<n and a[i] in s:
        i+=1
    if i<n and a[i]==b[j]:
        i+=1
        j+=1
    elif j<n and a[i]!=b[j]:
        s.add(b[j])
        ans+=1
        j+=1
print(ans)