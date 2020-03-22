n=int(input())
a=[int(o) for o in input().split()]
m=int(input())
b=[int(o) for o in input().split()]
s=a[:]+b[:]
s=set(s)
flag=0
for i in range(n):
    for j in range(m):
        if a[i]+b[j] not in s:
            print(a[i],b[j])
            flag=1
            break
    if flag==1:
        break