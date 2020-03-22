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
    n=int(input())
    lol=[]
    d=dict()
    d1=dict()
    for i in range(n):
        x,y,z=map(int,input().split())
        lol.append([x,y,z,i+1])
    lol.sort()
    for ii in range(n):
        x=lol[ii][0]
        y=lol[ii][1]
        z=lol[ii][2]
        i=lol[ii][3]-1
        try:
            d[str([x,y])].append(i+1)
        except:
            d[str([x,y])]=[i+1]
        try:
            d1[x].append(i+1)
        except:
            d1[x]=[i+1]
    vis=[False]*n
    ans=[]
    for i in d.values():
        #i.sort()
        if len(i)>=2:
            for j in range(len(i)//2):
                vis[i[j*2]-1]=True
                vis[i[j*2+1]-1]=True
                ans.append([i[j*2],i[j*2+1]])
    for i in d1.values():
       # i.sort()
        n1=len(i)
        if n1>=2:
            j=0
            k=1
            while k<n1:
                if vis[i[j]-1]==True:
                    j+=1
                if vis[i[k]-1]==True or j==k:
                    k+=1
                if k<n1 and vis[i[k]-1]==False and vis[i[j]-1]==False:
                    ans.append([i[k],i[j]])
                    vis[i[k]-1]=True
                    vis[i[j]-1]=True
    #lol=sorted(lol)
    i=0
    j=1
    c=0
    while j<n:
        if vis[lol[i][3]-1]==True:
            i+=1
        if vis[lol[j][3]-1]==True or j==i:
            j+=1
        if j<n and vis[lol[i][3]-1]==False and vis[lol[j][3]-1]==False:
            ans.append([lol[i][3],lol[j][3]])
            vis[lol[i][3]-1]=True
            vis[lol[j][3]-1]=True
    for i in ans:
        print(*i)
 
 
 
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()