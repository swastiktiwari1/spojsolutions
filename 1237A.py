n=int(input())
a=[0]*n
sa=[]
for i in range(n):
    a[i]=int(input())
    if a[i]%2!=0:
        sa.append(i)
    a[i]//=2
for i in range(abs(sum(a))):
    a[sa[i]]+=1
for i in range(n):
    print(a[i])