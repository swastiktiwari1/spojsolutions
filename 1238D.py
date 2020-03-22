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
    n=int(input())
    s=input()
    ans=(n*(n-1))//2
    #  print(ans)
    a=[]
    b=[]
    for i in range(n):
        if s[i]=="A":
            a.append(i)
        else:
            b.append(i)
    se=set()
    if a:
        for i in range(a[-1]+1,n):
            se.add(str([a[-1],i]))
        for i in range(a[0]):
            se.add(str([i,a[0]]))
    if b:
        for i in range(b[-1]+1,n):
            se.add(str([b[-1],i]))
        for i in range(b[0]):
            se.add(str([i,b[0]]))
    #  print(ans)
    la=len(a)
    for i in range(la):
        if i!=la-1:
            for j in range(a[i]+1,a[i+1]):
                se.add(str([a[i],j]))
        if i!=0:
            for j in range(a[i-1]+1,a[i]):
                se.add(str([j,a[i]]))
    lb=len(b)
    for i in range(lb):
        if i!=lb-1:
            for j in range(b[i]+1,b[i+1]):
                se.add(str([b[i],j]))
        if i!=0:
            for j in range(b[i-1]+1,b[i]):
                se.add(str([j,b[i]]))
    #print(se)
    print(ans-len(se))

if __name__ == '__main__':
    sync_with_stdio(False)
    main()