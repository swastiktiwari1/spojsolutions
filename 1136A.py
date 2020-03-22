n=int(input())
l=[None]*n
for i in range(n):
    l[i]=[int(o) for o in input().split()]
a=int(input())
s=0
for i in range(n):
    if a<=l[i][1] and a>=l[i][0]:
        s=n-i
        break
print(s)