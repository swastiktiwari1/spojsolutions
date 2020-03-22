import bisect
n=int(input())
a=[abs(int(o)) for o in input().split()]
a=sorted(a)
ans=0
for i in range(n):
        lol=2*a[i]
        ind=bisect.bisect(a,lol)
        ans+=(ind)-i-1
print(ans)