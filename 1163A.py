import heapq
n,m=map(int,input().split())
h=[]
heapq.heappush(h,-n+1)
for i in range(m-1):
    #print(h)
    k=heapq.heappop(h)
    if k<-2:
        heapq.heappush(h,k+2)
        heapq.heappush(h,-1)
    elif k==-2:
        heapq.heappush(h,-1)
print(len(h))