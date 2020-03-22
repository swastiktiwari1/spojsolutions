for _ in range(int(input())):
    n=int(input())
    s=input()
    clkd=n-1
    for i in range(n):
        if (s[0+i]==">" or s[n-i-1]=="<"):
            clkd=min(clkd,i)
    print(clkd)