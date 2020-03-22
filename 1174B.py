n=int(input())
a=[int(o) for o in input().split()]
ec,oc=0,0
for i in range(n):
    if a[i]%2==0:
        ec+=1
    else:
        oc+=1
if ec>0 and oc>0:
    a=sorted(a)
print(*a)