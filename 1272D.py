n=int(input())
a=[int(o) for o in input().split()]
arr=[1]*n
upto=[1]*n
c=1
for i in range(1,n):
   # print(c)
    flag=0
    if a[i-1]<a[i]:
        c+=1
       # print(i,c)
    
    else:
        flag=1
        for j in range(i-c,i):
            arr[j]=c
            c-=1
        c=1
    upto[i]=c
    if i==n-1 and flag==0:
        for j in range(i-c+1,i):
            #print(j)
            arr[j]=c
            c-=1
ca=max(arr)
#print(arr)
for i in range(1,n-1):
    if a[i-1]<a[i+1]:
        ca=max(ca,upto[i-1]+arr[i+1])
print(ca)