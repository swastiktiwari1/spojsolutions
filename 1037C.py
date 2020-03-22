import heapq
n=int(input())
a=input()
b=input()
a=list(a)
b=list(b)
h=[]
c=0
for i in range(n-1):
    if a[i]!=b[i]:
        if a[i+1]!=b[i+1] and a[i+1]!=a[i]:
            a[i],a[i+1]=a[i+1],a[i]
            c+=1
        else:
            c+=1
            a[i]=b[i]
if a[n-1]!=b[n-1]:
    c+=1
print(c)