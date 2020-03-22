import atexit
import io
import sys
import heapq
_INPUT_LINES = sys.stdin.read().splitlines()
raw_input = iter(_INPUT_LINES).next
_OUTPUT_BUFFER = io.BytesIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
def takla():
    
    
    n,m=map(int,raw_input().split())
    x=[int(o) for o in raw_input().split()]
    c=0
    i=1
    j=1
    k=0
    s=set(x)
    h=[]
    ans=[]
    for i in range(n):
        if x[i]-1 not in s:
            heapq.heappush(h,[1,-1,x[i]-1])
            
        if x[i]+1 not in s:
            heapq.heappush(h,[1,1,x[i]+1])
    while c!=m:
        lol=heapq.heappop(h)
        if lol[1]>0:
            if lol[2] not in s:
                s.add(lol[2])
                ans.append(lol[2])
                c+=1
                k+=lol[0]
                lol[1]+=1
                lol[0]+=1
                lol[2]+=1
                # c+=1
                if lol[2] not in s:
                    heapq.heappush(h,lol[:])
                    # c+=1
        else:
            if lol[2] not in s:
                s.add(lol[2])
                ans.append(lol[2])
                c+=1
                k+=lol[0]
                lol[1]-=1
                lol[0]+=1
                lol[2]-=1
                # c+=1
                if lol[2] not in s:
                    heapq.heappush(h,lol[:])
     
    print(k)
    for i in xrange(m):
        print ans[i],
          
    
if __name__ == "__main__":
	takla()