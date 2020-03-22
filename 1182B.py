h,w=map(int,input().split())
arr=[None]*h
for i in range(h):
    arr[i]=input()
    arr[i]=list(arr[i])
flag=0
has=[[0 for i in range(w)]for j in range(h)]
for i in range(1,h-1):
    
    for j in range(1,w-1):
        if arr[i][j]=="*" and arr[i+1][j]=="*" and arr[i-1][j]=="*" and arr[i][j+1]=="*" and arr[i][j-1]=="*" and arr[i-1][j-1]!="*" and arr[i+1][j-1]!="*" and arr[i+1][j+1]!="*" and arr[i-1][j+1]!="*":
            for i1 in range(i,h):
                if arr[i1][j]=="*":
                    has[i1][j]=1
                else:
                    break
            i1=i
            while i1>=0:
                if arr[i1][j]=="*":
                    has[i1][j]=1
                else:
                    break
                i1-=1
            for j1 in range(j,w):
                if arr[i][j1]=="*":
                    has[i][j1]=1
                else:
                    break
            j1=j
            while j1>=0:
                if arr[i][j1]=="*":
                    has[i][j1]=1
                else:
                    break
                j1-=1
            flag=1
            break
    if flag==1:
        break
flag1=0
for i in range(h):
    for j in range(w):
        if arr[i][j]=="*" and has[i][j]!=1:
            flag1=1
            break
    if flag1==1:
        break
if flag==1 and flag1==0:
    print("YES")
else:
    print("NO")