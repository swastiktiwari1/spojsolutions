for _ in range(int(input())):
    a=list(input())
    n=len(a)
    odd=[]
    even=[]
    for i in range(n):
        a[i]=int(a[i])
        if a[i]%2==0:
            odd.append(a[i])
        else:
            even.append(a[i])
    lo=len(odd)
    le=len(even)
    oi=0
    ei=0
    while oi<lo and ei<le:
        if odd[oi]<even[ei]:
            print(odd[oi],end="")
            oi+=1
        else:
            print(even[ei],end="")
            ei+=1
    
    for i in range(oi,lo):
        print(odd[i],end="")

    for i in range(ei,le):
        print(even[i],end="")
    print()