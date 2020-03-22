n=int(input())
a=[int(o) for o in input().split()]
mai=a.index(max(a))
a1=a[:mai]
a2=a[mai+1:]
a1.sort()
a2.sort()
a2=a2[::-1]
#print(a1,a2)
if a1+[a[mai]]+a2==a:
    print("YES")
else:
    print("NO")