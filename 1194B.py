for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[None]*n
    mc=0
    arr1=[]
    rs=[0]*n
    cs=[0]*m
    for i in range(n):
        arr[i]=list(input())
        for j in range(m):
            if arr[i][j]=="*":
                rs[i]+=1
                cs[j]+=1
    minmoves=(n+m-1)
    for i in range(n):
        for j in range(m):
            if arr[i][j]==".":
                minmoves=min(minmoves,n-rs[i]+m-cs[j]-1)
            else:
                minmoves=min(minmoves,n-rs[i]+m-cs[j])
           # print(rs[i]+cs[j],end=" ")
 #   print(rs)
  #  print(cs)
    print(minmoves)