a,b,c,d = sorted(map(int,input().split()))
if ((a+b+c) == d) or (a+d) == (c+b) :
    print("YES")
else:
    print("NO")