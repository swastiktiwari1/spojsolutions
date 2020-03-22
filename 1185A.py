
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
    a,b,c,d=map(int,input().split())
    lis=[[a,1],[b,2],[c,3]]
    lis=sorted(lis)
    s=d-(lis[1][0]-lis[0][0])
    s2=d-(lis[2][0]-lis[1][0])
    print(max(s2,0)+max(s,0))
        
        
if __name__ == '__main__':
    sync_with_stdio(False)
    main()