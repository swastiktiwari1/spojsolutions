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
 
def isprime(x):
    if x==1:
        return False
    if x==2:
        return True
    flag=0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    else:
        return True 
def main():
    n=int(input())
    a=[int(o) for o in input().split()]
    tc=a.count(2)
    oc=a.count(1)
    c=0
    while tc>0 or oc>0:
        if oc>0:
            if isprime(c+1):
                print("1",end=" ")
                c+=1
                oc-=1
            elif tc>0:
                print("2",end=" ")
                c+=2
                tc-=1
            else:
                print("1",end=" ")
                c+=1
                oc-=1
        else:
            print("2",end=" ")
            c+=2
            tc-=1


            
    
if __name__ == '__main__':
    sync_with_stdio(False)
    main()