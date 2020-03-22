n=int(input())
arr=[int(o) for o in input().split()]
d=[0]*n
d[0]=200000
for i in range(1,n):
    d[i]=arr[i-1]+d[i-1]
do=min(d)
for i in range(n):
    d[i]=d[i]-(do-1)
    
if len(set(d))==n and max(d)==n:
    print(*d)
else:
    print("-1")