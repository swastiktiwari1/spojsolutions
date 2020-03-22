from collections import Counter
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
raw_input = iter(_INPUT_LINES).next
_OUTPUT_BUFFER = io.BytesIO()
sys.stdout = _OUTPUT_BUFFER
 
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
def takla():
    n,m,k=map(int,raw_input().split())
    a=[int(o) for o in raw_input().split()]
    b=[int(o) for o in raw_input().split()]
    a.append(0)
    b.append(0)
    for i in range(n):
        a[i]=(a[i-1]+1 if a[i]==1 else 0)
    d=dict(Counter(a))
    # print(d)
    dk=sorted(list(d.keys()))
    dk=dk[::-1]
    dk.pop()
    for i in range(1,len(dk)):
        d[dk[i]]+=d[dk[i-1]]
    # print(d)
    ans=0
    for i in range(m):
        b[i]=(b[i-1]+1 if b[i]==1 else 0)
    d1=dict(Counter(b))
    # print(d)
    dk=sorted(list(d1.keys()))
    dk=dk[::-1]
    dk.pop()
    for i in range(1,len(dk)):
        d1[dk[i]]+=d1[dk[i-1]]
    for j in d1.keys():
        if j!=0:
            if j<=k and k%j==0:
                k1=k//j
                if k1 in d:
                    # print(k1,j)
                    ans+=(d[k1]*d1[j])
    # print(d)
    # print(d1)
    print(ans)
    
      
    
if __name__ == "__main__":
	takla()