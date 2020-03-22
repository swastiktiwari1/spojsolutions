n=int(input())
a=[int(o) for o in input().split()]
pos=[]
neg=[]
res=0
z=0
for i in range(n):
    if a[i]<0:
        neg.append(a[i])
        res+=abs(a[i]+1)
    elif a[i]>0:
        pos.append(a[i])
        res+=(abs(a[i]-1))
    else:
        z+=1
        res+=1
#print(res)
if (len(neg))%2!=0 and z==0:
    res+=2
print(res)