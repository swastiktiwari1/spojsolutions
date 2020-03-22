n=int(input())
a=[int(o) for o in input().split()]
o=0
e=0
for i in a:
    if i%2==0:
        e+=1
    else:
        o+=1
print(min(e,o))