from collections import Counter
n=int(input())
a=[int(o) for o in input().split()]
a=sorted(a)
i=0
j=0
su=0
a=sorted(a)
while i<len(a):
    if a[i]>j:
        su+=(a[i]-j)
        a[i]-=j
    j+=1
    i+=1     
print("cslnb" if su%2==0 and len(a)==len(set(a)) else "sjfnb")