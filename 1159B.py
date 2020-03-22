n=int(raw_input())
a=[int(o) for o in raw_input().split()]
kk=[]
for i in range(n):
    de=max(i,n-i-1)
    kk.append(a[i]/de)
print(min(kk))