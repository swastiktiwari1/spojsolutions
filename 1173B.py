n=int(input())
a=[[0 for i in range(n)]for j in range(n)]
arr=[None]*10001
a[0]=[1,1]
a[0][0]=1
row=1
col=2
arr[0]=[1,1]
arr[1]=[1,2]
i=2
while i<=n:
    if i%2!=0:
        col+=1
    else:
        row+=1
    arr[i]=[row,col]
    i+=1
ans=max(arr[n-1])
print(ans)
for i in range(n):
    print(*arr[i])