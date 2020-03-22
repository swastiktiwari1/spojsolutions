n=int(input())
a=[int(o) for o in input().split()]
ma=0
i=0
d=0
while i<n:
    ma=a[i]-1
    while i<=ma:
        
        if a[i]-1>ma:
            ma=a[i]-1
        i+=1
    #print(ma)
    
    d+=1
print(d)