n=int(input())
a=[int(o) for o in input().split()]
s=sum(a)
m=max(a)
print("YES" if (s%2==0 and m<=(s-m)) else "NO")