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
def lp(s):
    kmprev=s[::-1]
    kmp=s+"#"+kmprev
    lps=[0]*(len(kmp))
    for i in range(1,len(lps)):
        prev_idx=lps[i-1]
        while (prev_idx > 0 and kmp[i] != kmp[prev_idx]):
            prev_idx = lps[prev_idx - 1];
    
        lps[i] = prev_idx + (1 if (kmp[i] == kmp[prev_idx]) else 0)
    # print(lps)
    return lps[-1]
def takla():
    for _ in range(int(input())):
        s=input()
        n=len(s)
        i=0
        j=n-1
        ans=[]
        while s[i]==s[j] and i<j:
            ans.append(s[i])
            i+=1
            j-=1
        lol=s[i:j+1]
        k1=lp(lol)
        k2=lp(lol[::-1])
        ansr=ans[::-1]
        if k1>k2:
            ans.append(lol[:k1])
        else:
            ans.append(lol[::-1][:k2])
        ans+=ansr
        print "".join(ans)
        
if __name__ == "__main__":
	takla()