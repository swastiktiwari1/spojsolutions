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
    for _ in range(int(raw_input())):
        r,c=map(int,raw_input().split())
        arr=[None]*r
        f0,f1,f2,f3,f4=0,0,0,0,0
        rs="A"*c
        fs=""
        ls=""
        jkj=0
        for i in range(r):
            arr[i]=raw_input()
            if arr[i]==rs:
                if i==0 or i==r-1:
                    f1+=1
                f2+=1
                jkj+=1
            for j in range(c):
                if arr[i][j]=="A":
                    if (i==0 or i==r-1):
                        f3+=1
                    if (j==0 or j==c-1):
                        f3+=1
                    if (j==0 or j==c-1) and (i==0 or i==r-1):
                        f2+=1
                    f4+=1
            fs+=arr[i][0]
            ls+=arr[i][c-1]
        for j in range(c):
            lll=0
            for i in range(r):
                if arr[i][j]=="A":
                    lll+=1
            if lll==r:
                f2+=1
        cs="A"*r
        if jkj==r:
            f0+=1
        if fs==cs or ls==cs:
            f1+=1
        if f0>0:
            print("0")
        elif f1>0:
            print("1")
        elif f2>0:
            print("2")
        elif f3>0:
            print(3)
        elif f4>0:
            print("4")
        else:
            print("MORTAL")
      
    
if __name__ == "__main__":
	takla()