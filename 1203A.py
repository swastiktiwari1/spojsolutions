for _ in range(int(input())):
    n=int(input())
    a=[int(o) for o in input().split()]
    arr=[0]*(n)
    for i in range(n):
        arr[i]=a[i]-a[(i+1)%n]
    if arr.count(1)==n-1 or arr.count(-1)==n-1:
        print("YES")
    else:
        print("NO")