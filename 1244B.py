for _ in range(int(input())):
    n=int(input())
    s=input().strip()
    if "1" in s:
        index1=n-s.index("1")
        index2=n-s[::-1].index("1")
        print(max(index1,index2)*2)
        
    else:
        print(n)