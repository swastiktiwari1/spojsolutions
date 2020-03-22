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
    s=list(input())
    n1=n
    alph=list("qwertyuiopasdfghjklzxcvbnm")
    alph.sort()
    alph=alph[::-1]
    j=0
    flag=0
    while True:
        lf=0
        for i in range(n):
            if s[i]==alph[j] and  ( (i+1<n and s[i+1]==alph[j+1]) or (i-1>=0 and s[i-1]==alph[j+1]) ):
                s.pop(i)
                n-=1
                lf=1
                break
        if lf==0:
            j+=1
        if j==25:
            break
    print(n1-n)
      
    
if __name__ == "__main__":
	takla()