def bfs(start):
    global count
    queue = []
    queue.append(start)
  # mark the start node as visited
    visited[start] = True
    count+=1
    while queue:
    # Dequeue the oldest vertex from queue
        start = queue.pop(0)
    # Printing the dequeued vertex
    #print start,
    # Get all the adjacent vertices of the dequeued vertex
        for i in range(len(adj[start])):
            ele = adj[start][i]
      # Enqueue the vertex if unvisited and mark as visited
            if not visited[ele]:
                visited[ele] = True
                count+=1
                queue.append(ele)
n,k=map(int,input().split())
adj=[[] for i in range(n)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    if c==0:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
visited=[False]*n
ca=[]
for i in range(n):
    if not(visited[i]):
        count=0
        bfs(i)
        ca.append(count)
ans=0
mod=(10**9)+7
pa=pow(n,k,mod)
for i in ca:
    ans=(ans+pow(i,k,mod))%mod
print((pa-ans)%mod)