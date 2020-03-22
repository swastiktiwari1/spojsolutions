
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
    n=int(input())
    for i in range(n):
        a1=input()
        a2=input()
        i=0
        j=0
        f=0
        la1=len(a1)
        la2=len(a2)
        a1+="0"
        a2+="0"
    
        a1m=[]
        a2m=[]
        for i in range(la1):
            if a1[i]==a1[i-1]:
                a1m[-1]+=1
            else:
                a1m.append(a1[i])
                a1m.append(1)
        for i in range(la2):
            if a2[i]==a2[i-1]:
                a2m[-1]+=1
            else:
                a2m.append(a2[i])
                a2m.append(1)
       # print(a1m)
        #print(a2m)
        if len(a1m)!=len(a2m):
            print("NO")
        else:
            f=0
            for i in range(len(a1m)//2):
                if a1m[2*i]!=a2m[2*i]:
                    f=1
                    break
                if int(a1m[2*i+1])>int(a2m[2*i+1]):
                    f=1
                    break
            print("YES" if f==0 else "NO")
                
        
if __name__ == '__main__':
    sync_with_stdio(False)
    main()