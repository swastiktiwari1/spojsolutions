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
    for _ in range(int(input())):
        n,m=map(int,input().split())
        adj=[[] for i in range(n)]
        for i in range(m):
            a,b=map(int,input().split())
            adj[a-1].append(b-1)
            adj[b-1].append(a-1)
        visited=[False]*n
        q=deque()
        q.append(0)
        dist=[0]*n
        visited[0]=True
        while q:
            s=q.popleft()
            for i in adj[s]:
                if not(visited[i]):
                    dist[i]=dist[s]+1
                    visited[i]=True
                    q.append(i)
        odd=[]
        even=[]
        for i in range(n):
            if dist[i]%2==0:
                even.append(i+1)
            else:
                odd.append(i+1)
        if len(even)<len(odd):
            print(len(even))
            print(*even)
        else:
            print(len(odd))
            print(*odd)
if __name__ == '__main__':
    sync_with_stdio(False)
    main()