import sys
sys.setrecursionlimit(100000000)
def getdfs():
    for i in range(n):
        if not visited[i]:
            he_kya[i]=dfs(i)
def dfs(s):
    visited[s]=True
    for i in adj[s]:
        if not visited[i]:
            color[i]=not(color[s])
            if not dfs(i):
                return False
        elif color[s]==color[i]:
            return False
    return True
            
for _ in range(int(input())):
    n,m=map(int,input().split())
    adj=[None]*n
    for i in range(n):
        adj[i]=[]
    for i in range(m):
        a,b=map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    he_kya=[True]*n
    visited=[False]*n
    color=[False]*n
    d=[]
    getdfs()
    g=1
    print("Scenario #"+str(_+1)+":")
    print("Suspicious bugs found!" if False in he_kya else "No suspicious bugs found!")
    
