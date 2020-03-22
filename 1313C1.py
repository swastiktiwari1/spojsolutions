from collections import Counter
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).next
_OUTPUT_BUFFER = io.BytesIO()
sys.stdout = _OUTPUT_BUFFER
 
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
def takla():
    n=int(input())
    a=[int(o) for o in input().split()]
    lol=[]
    for i in range(n):
        a1=a[:]
        for j in range(i-1,-1,-1):
            a1[j]=min(a1[j+1],a1[j])
        for j in range(i+1,n):
            a1[j]=min(a1[j-1],a[j])
        lol.append([sum(a1),a1[:]])
    k=max(lol)
    for i in k[1]:
        print i,
    
if __name__ == "__main__":
	takla()