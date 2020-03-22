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
    from math import ceil
    n,l,r=map(int,input().split())
    a=int((r//3)-ceil(l/3)+1)
    b=int(((r-1)//3)-ceil((l-1)/3)+1)
    c=int(((r-2)//3)-ceil((l-2)/3)+1)
    dp=[[0 for i in range(3)] for j in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        dp[i][0]=((dp[i-1][0]*a)+dp[i-1][1]*c+dp[i-1][2]*b)%1000000007
        dp[i][1]=((dp[i-1][0]*b)+dp[i-1][1]*a+dp[i-1][2]*c)%1000000007
        dp[i][2]=((dp[i-1][0]*c)+dp[i-1][1]*b+dp[i-1][2]*a)%1000000007
    print(int(dp[n][0]))

if __name__ == '__main__':
    sync_with_stdio(False)
    main()