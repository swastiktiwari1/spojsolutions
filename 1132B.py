n=int(input())
a=[int(o) for o in input().split()]
a=sorted(a)
a=a[::-1]
m=int(input())
s=sum(a)
d=[int(o) for o in input().split()]
for i in d:
    print(s-a[i-1])