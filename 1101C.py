import bisect
for _ in range(int(input())):
    n=int(input())
    arr=[]
    seg=[0]*n
    cs=1
  
    for i in range(n):
        a=list(map(int,input().split()))
        a.append(i)
        bisect.insort(arr,a)
    seg[arr[0][2]]=1
    pm=arr[0][1]
    for i in range(1,n):
        if arr[i][0]<=pm:
            pm=max(pm,arr[i][1])
            seg[arr[i][2]]=cs
        else:
            cs=2
            seg[arr[i][2]]=cs
    if len(set(seg))!=2:
        print("-1")
    else:
        print(*seg)