for _ in range(int(input())):
    b,p,f=map(int,input().split())
    h,c=map(int,input().split())
  #  p=0
    arr=[c]*(f)+[h]*p
    
    arr=sorted(arr)
    pr=0
    i=0
   # print(arr)
    while b>1 and arr:
        
        pr+=arr.pop()
        b-=2

    print(pr)