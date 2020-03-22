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
        n=int(input())
        l=-100000
        t=100000
        r=100000
        d=-100000
        for i in range(n):
            a,b,t1,t2,t3,t4=map(int,input().split())
    
            if(t1==0):
                l=max(l,a)
            if(t2==0):
                t=min(t,b)
            if(t3==0):
                r=min(r,a)
            if(t4==0):
                d=max(d,b)  
        if(l<=r and d<=t):
            print("1",l,t)
        else:
            print("0")
        

if __name__ == '__main__':
    sync_with_stdio(False)
    main()