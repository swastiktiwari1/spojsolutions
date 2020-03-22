a=[int(o) for o in  input().split()]
a=sorted(a)
a=a[::-1]
if a[1]+a[2]>a[0] or a[2]+a[3]>a[1]:
    print("TRIANGLE")
elif a[1]+a[2]==a[0] or a[2]+a[3]==a[1]:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")