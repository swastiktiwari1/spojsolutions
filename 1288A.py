import math
for  _ in range(int(input())):
    n,d=map(int,input().split())
    low=0
    high=n
    while low<=high:
        mid=(low+high)//2
        if mid+math.ceil(d/(mid+1))>n:
            low=mid+1
        else:
            high=mid-1
    # print(low,low+math.ceil(d/(low+1)))
    if  low+math.ceil(d/(low+1))<=n:
        print("YES")
    else:
        print("NO")