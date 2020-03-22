n=int(input())
arr=[None]*n
for i in range(n):
    arr[i]=list(input())
flag=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==".":
            try:
                if j>=1 and arr[i+1][j]=="." and arr[i+2][j]=="." and arr[i+1][j+1]=="." and arr[i+1][j-1]==".":
                    arr[i][j]="#"
                    arr[i+1][j]="#"
                    arr[i+2][j]="#"
                    arr[i+1][j+1]="#"
                    arr[i+1][j-1]="#"
                else:
                    flag=1
                    break
            except:
                flag=1
                break
    if flag==1:
        break
print("YES" if flag==0 else "NO")