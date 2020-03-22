from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
from atexit import register
from collections import Counter
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

    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    psa=[0]*(n+1)
    for i in range(n):
        psa[i]=psa[i-1]+a[i]
    s=0
    #print(psa)
    for i in range(n-k+1):
        for j in range(k,n-i+1):
            #(print(i,i+j-1))
            #print((psa[i+j]-psa[i-1])/j)
            if (psa[i+j-1]-psa[i-1])/j>s:
                s=(psa[i+j-1]-psa[i-1])/(j)
    print(s)
            
    
if __name__ == '__main__':
    sync_with_stdio(False)
    main()