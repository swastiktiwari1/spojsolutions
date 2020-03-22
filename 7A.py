ans=0
arr=[None]*8
for i in range(8):
    arr[i]=list(input())
    if arr[i].count("B")==8:
        arr[i]=["W"]*8
        ans+=1
for i in range(8):
    for j in range(8):
        if arr[i][j]=="B":
            ans+=1
            for k in range(8):
                arr[k][j]="W"
print(ans)