n=int(input())
a=[int(o) for o in input().split()]
s=sum(a)
ans=[1]
cs=a[0]
for i in range(1,n):
    if a[i]*2<=(a[0]):
        cs+=a[i]
        ans.append(i+1)
if cs>=(s//2)+1:
    print(len(ans))
    print(*ans)
else:
    print("0")
   # print(ans)