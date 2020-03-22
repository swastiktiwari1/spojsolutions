n=int(input())
a=[int(o) for o in input().split()]
u=max(a)
ml=1
l=1
for i in range(n-1):
    
    if a[i]==u and a[i+1]==u:
        l+=1
        if l>ml:
            ml=l
    else:
        l=1
    
print(ml)