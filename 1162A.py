n,h,m=map(int,input().split())
arr=[h**2]*n
for i in range(m):
    a,b,c=map(int,input().split())
    for j in range(a-1,b):
        arr[j]=min(arr[j],c**2)
print(sum(arr))