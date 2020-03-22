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
    s=input()
    n=len(s)
    d=dict(Counter(s))
    ans=-float('inf')
    for i in d:
        ans=max(ans,d[i])
    d2=dict()
    for i in range(n):
       d[s[i]]-=1
       for j in d:
            try:
                d2[s[i]+j]+=d[j]
            except:
                d2[s[i]+j]=d[j]
        
    for i in d2:
        ans=max(ans,d2[i])
    print(ans)
    
if __name__ == "__main__":
	takla()