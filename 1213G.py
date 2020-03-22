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

res=0
n,m=map(int,input().split())
dsu=[i for i in range(n)]
size=[1]*n
def find(x):
    global res
    while x!=dsu[x]:
        dsu[x]=dsu[dsu[x]]
        x=dsu[x]
    return x
def union(x,y):
    global res
    fx=find(x)
    fy=find(y)
    sfx=size[fx]
    sfy=size[fy]
    ts=sfx+sfy
    if fx==fy:
        return
    if sfx>sfy:
        res=res-(sfx*(sfx-1)//2)-(sfy*(sfy-1)//2)+(ts*(ts-1)//2)
        size[fx]+=size[fy]
        dsu[fy]=fx
        return
    else:
        res=res-(sfx*(sfx-1)//2)-(sfy*(sfy-1)//2)+(ts*(ts-1)//2)
        size[fy]+=size[fx]
        dsu[fx]=fy
        return

def main():
    edges=[]

    for i in range(n-1):
        a,b,c=map(int,input().split())
        edges.append([c,a-1,b-1])
    edges.sort()
    #dsu=[i for i in range(n)]
    #size=[1]*n
    q=[int(o) for o in input().split()]
    q1=[[q[i],i] for i in range(m)]
    q1=sorted(q1)
    j=0
    answer=[0]*m
    for i in range(m):
        while j<n-1 and edges[j][0]<=q1[i][0]:
            union(edges[j][1],edges[j][2])
            j+=1
        
        answer[q1[i][1]]=res
    print(*answer)

if __name__ == '__main__':
    sync_with_stdio(False)
    main()