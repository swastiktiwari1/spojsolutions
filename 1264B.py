a,b,c,d=map(int,input().split())
arr=[]
for i in range(c):
    arr.append(-1)
    arr.append(2)
for i in range(a):
    arr.append(-1)
    arr.append(0)
arr.append(-1)
la=len(arr)
i=0
# print(arr)
while d>0 and i<la:
    if arr[i]==-1:
        if i>0 and i!=la-1 and arr[i-1]==2 and arr[i+1]==2:
            arr[i]=3
            d-=1
        elif i==0 and i!=la-1 and arr[i+1]==2:
            arr[i]=3
            d-=1
        elif i==la-1 and i!=0 and arr[i-1]==2:
            arr[i]=3
            d-=1
        elif la-1==0 :
            arr[i]=3
            d-=1
        i+=1
    else:
        i+=1
i=la-1
while i>=0 and b>0:
    if arr[i]==-1:
        arr[i]=1
        b-=1
    i-=1
# print(arr)
flag=0
for i in range(1,la):
    if arr[i]==-1:
        if i>0 and i!=la-1 and arr[i-1]==2 and arr[i+1]==2 and flag==0 and arr[0]!=-1:
            arr[i],arr[0]=arr[0],arr[i]
           # print("YEY")
            flag=1
        elif flag==1 or flag==0:
            # print("vhk",arr[i],arr[-1])
            arr[i],arr[-1]=arr[-1],arr[i]
            # print("vhk",arr[i],arr[-1])
            flag=2
        elif i!=la-1:
            flag=777
# print(arr)
ans=[]
if arr.count(-1)<=2 and b==0 and d==0 and flag!=777:
    for i in arr:
        if i!=-1:
            ans.append(i)
    flag=0
    for i in range(1,len(ans)):
        if abs(ans[i]-ans[i-1])!=1:
            flag=777
            # print("vknj")
if flag==0 and ans:
    print("YES")
    print(*ans)
else:
    print("NO")