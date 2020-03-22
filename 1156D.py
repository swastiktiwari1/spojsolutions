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
    def union0(a,b):
        fa=find0(a)
        fb=find0(b)
        if size0[fa]>size0[fb]:
            size0[fa]+=size0[fb]
            dsu0[fb]=fa
        else:
            size0[fb]+=size0[fa]
            dsu0[fa]=fb
    def union1(a,b):
        fa=find1(a)
        fb=find1(b)
        if size1[fa]>size1[fb]:
            size1[fa]+=size1[fb]
            dsu1[fb]=fa
        else:
            size1[fb]+=size1[fa]
            dsu1[fa]=fb
    def find0(x):
        while dsu0[x]!=x:
            dsu0[x]=dsu0[dsu0[x]]
            x=dsu0[x]
        return x
    def find1(x):
        while dsu1[x]!=x:
            dsu1[x]=dsu1[dsu1[x]]
            x=dsu1[x]
        return x
     
            
    n=int(input())
    edges=[]
    for i in range(n-1):
        a,b,c=map(int,input().split())
        edges.append([c,a-1,b-1])
    size0=[1]*n
    size1=[1]*n
    dsu1=[i for i in range(n)]
    dsu0=[i for i in range(n)]
    edges.sort()
    ans=0
    for i in range(n-1):
        if edges[i][0]==0:
            fa=find0(edges[i][1])
            fb=find0(edges[i][2])
            ans+=2*(size0[fa]*size0[fb])
            union0(fa,fb)
        else:
            fa=find1(edges[i][1])
            fb=find1(edges[i][2])
            ans+=2*(size1[fa]*size1[fb])
            union1(fa,fb)
    for i in range(n):
        f0=find0(i)
        f1=find1(i)
        ans+=((size0[f0]-1)*(size1[f1]-1))
    print(ans)

if __name__ == '__main__':
    sync_with_stdio(False)
    main()