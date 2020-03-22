def bfs(s):
    q=[s]
    visited[s]=True
    while q:
        s=q.pop(0)
        for i in range(n):
            if adj[s][i]=="1":
                if not(visited[i]):
                    paths[j][i]=paths[j][s]+1
                    visited[i]=True
                    q.append(i)
 
n=int(input())
adj=[None]*n
for i in range(n):
    adj[i]=input()
m=int(input())
p=[int(o) for o in input().split()]
paths=[dict() for i in range(n)]
for j in range(n):
    visited=[False]*n
    paths[j][j]=0
    bfs(j)
stack=[p[0]-1]
ans = [p[0]]
cur = 1
while cur < m-1:
	if ans[-1] == p[cur + 1]:
		ans.append(p[cur])
	elif paths[ans[-1]-1][p[cur]-1] + paths[p[cur]-1][p[cur+1]-1] > paths[ans[-1]-1][p[cur+1]-1]:
		ans.append(p[cur])
	cur += 1
ans.append(p[-1])
print(len(ans))
print(*ans)