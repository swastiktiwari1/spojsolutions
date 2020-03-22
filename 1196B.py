from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
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
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        oc=0
        ans=[]
        for i in range(n):
            if a[i]%2!=0:
                oc+=1
                ans.append(i+1)
        if oc<k:
            print("NO")
        elif (oc-k-1)%2==0:
            print("NO")
        else:
            print("YES")
            print(*(ans[:k-1]+[n]))
        

if __name__ == '__main__':
    sync_with_stdio(False)
    main()