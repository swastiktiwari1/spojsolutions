from __future__ import division, print_function
import bisect
import math
import itertools
import sys
from atexit import register

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
    n,m=map(int,input().split())
    a=[int(o) for o in input().split()]
    b=[int(c) for c in input().split()]
    eca,oca,ecb,ocb=0,0,0,0
    for i in range(n):
        if a[i]%2==0:
            eca+=1
        else:
            oca+=1
    for i in range(m):
        if b[i]%2==0:
            ecb+=1
        else:
            ocb+=1
    print(min(eca,ocb)+min(oca,ecb))
if __name__ == '__main__':
    sync_with_stdio(False)
    main()