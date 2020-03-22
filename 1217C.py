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
    for _ in range(int(input())):
        s=input()
        ls=len(s)
        se=set()
        non=[0]*(ls+1)
        no=-1
        for i in range(ls):
            non[i]=no
            if s[i]=="1":
                no=i
        for i in range(1,19):
            for j in range(ls-i+1):
                lol=int(str(s[j:i+j]),base=2)
                if lol==i:
                    se.add(str([lol,j+i]))
                elif lol!=0 and j-non[j]>=(lol-i+1):
                    if j+i-lol>=0:
                        se.add(str([lol,j+i]))
                        
        print(len(se))
if __name__ == '__main__':
    sync_with_stdio(False)
    main()