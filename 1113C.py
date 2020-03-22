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
def binomialCoef(n, k): 
    C = [[0 for x in range(k+1)] for x in range(n+1)] 
  
    # Calculate value of Binomial Coefficient in bottom up manner 
    for i in range(n+1): 
        for j in range(min(i, k)+1): 
            # Base Cases 
            if j == 0 or j == i: 
                C[i][j] = 1
  
            # Calculate value using previously stored values 
            else: 
                C[i][j] = C[i-1][j-1] + C[i-1][j] 
  
    return C[n][k] 
    
def main():
    n=int(input())
    a=[int(o) for o in input().split()]
    pa=[0]*n
    ed=dict()
    od=dict()
    od[0]=1
    ed[a[0]]=1
    pa[0]=a[0]
    for i in range(1,n):
        pa[i]=pa[i-1]^a[i]
        if i%2==0:
            try:
                ed[pa[i]]+=1
            except:
                ed[pa[i]]=1
        else:
            
            try:
                od[pa[i]]+=1
            except:
                od[pa[i]]=1
    #print(pa)
    no=0
    for i in ed.values():
        no+=binomialCoef(i,2)
    for i in od.values():
        no+=binomialCoef(i,2)
    print(no)
    
    
            
    
if __name__ == '__main__':
    sync_with_stdio(False)
    main()