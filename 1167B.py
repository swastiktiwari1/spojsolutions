import sys
arr=[]
ar1=[4 , 8, 15, 16, 23, 42 ]
for i in range(5):
    for j in range(i+1,6):
        arr.append([ar1[i],ar1[j],ar1[i]*ar1[j]])
j=[]
for ll in range(4):
    print("?",ll+1,ll+2)
    sys.stdout.flush()
    k=int(input())
    for i in range(len(arr)):
        if k==arr[i][2]:
            j.append([arr[i][0],arr[i][1]])
print("!",end=" ")
dd=[]
if j[0][0] not in j[1]:
    dd.append(j[0][0])
else:
    dd.append(j[0][1])
for i in range(4):
    for jj in range(2):
        if dd[-1]!=j[i][jj]:
            dd.append(j[i][jj])
            break
for i in ar1:
    if i not in dd:
        dd.append(i)
print(*dd)
sys.stdout.flush()