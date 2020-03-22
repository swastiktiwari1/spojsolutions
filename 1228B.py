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
    h,w=map(int,input().split())
    arr=[[-1]*w for i in range(h)]
    lol=[int(o) for o in input().split()]
    for i in range(h):
        for j in range(lol[i]):
            arr[i][j]=1
        if lol[i]<w:
            arr[i][lol[i]]=0
    lol=[int(o) for o in input().split()]
    flag=0
    for i in range(w):
        for j in range(lol[i]):
            if arr[j][i]!=0:
                arr[j][i]=1
            else:
                flag=1
        if lol[i]<h:
            if arr[lol[i]][i]==0 or arr[lol[i]][i]==-1:
                arr[lol[i]][i]=0
            else:
                flag=1
    zz=0
    for i in range(h):
        zz+=arr[i].count(-1)
      #  print(arr[i])
    if flag==0:
        print(pow(2,zz,1000000007))
    else:
        print("0")
     #   print(pow(2,zz,1000000007))




    


if __name__ == '__main__':
    sync_with_stdio(False)
    main()