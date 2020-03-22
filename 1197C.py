n,k=map(int,input().split())
a=[int(o) for o in input().split()]
s=0
arr=[]
for i in range(1,n):
    arr.append(a[i]-a[i-1])
    s+=a[i]-a[i-1]
arr=sorted(arr)
arr=arr[::-1]
print(s-sum(arr[:k-1]))