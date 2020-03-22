import math
for _ in range(int(input())):
    n,x=map(int,input().split())
    arr=[None]*n
    for i in range(n):
        arr[i]=[int(o) for o in input().split()]
    marr=max(arr)
    if marr[0]>=x:
        print("1")
    else:
        tbc=[]
        for i in range(n):
            if arr[i][0]>arr[i][1]:
                tbc.append(arr[i][0]-arr[i][1])
        x=x-(marr[0])
        if tbc:
            mtb=max(tbc)
          #  print(x,mtb)
            print(int(math.ceil(x/mtb)+1))
        else:
            print("-1")