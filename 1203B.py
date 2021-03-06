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
        a=[int(o) for o in input().split()]
        a=sorted(a)
        d=dict(Counter(a))
        arr=[]
        for i in d.keys():
            if d[i]%2==0:
                arr.append([i,d[i]//2])
        larr=len(arr)
        d=dict()
        for i in range(larr):
            for j in range(i,larr):
                if arr[i][1]==arr[j][1]:
                    if i!=j:
                        try:
                            d[arr[i][0]*arr[j][0]]+=(arr[i][1])
                        except:
                            d[arr[i][0]*arr[j][0]]=(arr[i][1])
                    else:
                        try:
                            d[arr[i][0]*arr[j][0]]+=(arr[i][1])//2
                        except:
                            d[arr[i][0]*arr[j][0]]=(arr[i][1])//2
       # print(arr,d)
        print("YES" if n in d.values() else "NO")
if __name__ == '__main__':
    sync_with_stdio(False)
    main()