for i in range(int(input())):
    s,i,e = list(map(int,input().split()))
    print(max(0,min(e+1,(s-i+e+1)//2)))