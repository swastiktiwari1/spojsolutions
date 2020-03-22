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
    n,I=map(int,input().split())
    a=[int(o) for o in input().split()]
    a=sorted(a)
    pv=1<<((I*8//n))
    b=sorted(list(set(a)))
    d=dict(Counter(a))
    e=[]
    lb=len(b)
    prefix=[0]*(lb)
    for i in range(lb):
        prefix[i]=prefix[i-1]+d[b[i]]
    mi=n
    prefix.append(0)
    for i in range(lb):
        mi=min(mi,n-(prefix[min(i+pv-1,lb-1)]-prefix[i-1]))
    print(mi)


if __name__ == '__main__':
    sync_with_stdio(False)
    main()