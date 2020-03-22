n=int(input())
arr=[int(o) for o in input().split()]
z=[0]*n
arr=sorted(arr)
if arr[n-1]>=arr[n-2]+arr[n-3]:
    print("NO")
else:
    print("YES")
    for i in range(n-2):
        print(arr[i],end=" ")
    print(arr[n-1],arr[n-2])