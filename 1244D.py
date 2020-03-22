from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
from collections import deque
from atexit import register
from collections import Counter
from functools import reduce
sys.setrecursionlimit(10000000)
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
 
 
if sys.version_info[0] < 3:
    class dict(dict):
        """dict() -> new empty dictionary"""
        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)
 
        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)
 
        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)
 
    input = raw_input
    range = xrange
 
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
 
 
def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.
 
    Args:
        sync (bool, optional): The new synchronization setting.
 
    """
    global input, flush
 
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip('\r\n')
 
        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
 
def main():
   # from collections import Counter
   # import math
 #   from collections import deque
    n=int(input())
    cost=[None]*3
    for i in range(3):
        cost[i]=[int(o) for o in input().split()]
    adj=[[] for i in range(n)]
    indegree=[0]*n
    flag=0
    for i in range(n-1):
        a,b=map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
        indegree[a-1]+=1
        indegree[b-1]+=1
        if indegree[a-1]>2:
            flag=1
        if indegree[b-1]>2:
            flag=1
    if flag==1:
        print("-1")
    else:
        z=indegree.index(1)
        vis=[False]*n
        q=deque()
        q.append(z)
        ts=[z]
        vis[z]=True
        while q:
            s=q.popleft()
            for i in adj[s]:
                if not vis[i]:
                    vis[i]=True
                    ts.append(i)
                    q.append(i)
       # print(ts)
        arr=[[0]*n for i in range(6)]
        ps=[[0,1,2],[0,2,1],[1,2,0],[1,0,2],[2,0,1],[2,1,0]]
        mc=float('inf')
        ind=0
        for i in range(6):
            c=0
            for j in range(n):
                arr[i][ts[j]]=ps[i][j%3]+1
                c+=cost[ps[i][j%3]][ts[j]]
            if c<mc:
                mc=c
                ind=i
        print(mc)
        print(*arr[ind])
    
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()