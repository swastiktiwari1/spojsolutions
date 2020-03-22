from __future__ import division, print_function
import bisect
import math
import itertools
import sys
from atexit import register
from collections import Counter

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
    q=int(input())
    for i in range(q):
        n=int(input())
        a=list(map(int,input().split()))
        d=dict(Counter(a))
        ld=len(d)
        psa=[0]*ld
        j=0
        for i in d.values():
            psa[j]=i
            j+=1
        psa=sorted(psa)
        psa=psa[::-1]
        dd=0
        pre=-1
        c=dict()
        for i in range(ld):
            while psa[i] in c and psa[i]>=0:
                psa[i]-=1
            if psa[i]>=0:
                c[psa[i]]=1
                dd+=psa[i]
        print(dd)
    
if __name__ == '__main__':
    sync_with_stdio(False)
    main()