import heapq
n=int(raw_input())
a=[int(o) for o in raw_input().split()]
h=[]
for i in range(n):
    heapq.heappush(h,a[i])
i=1
s=0
while h:
    g=heapq.heappop(h)
    if g>=i:
        s+=1
        i+=1
print(s)