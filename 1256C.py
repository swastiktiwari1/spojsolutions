n,m,d=map(int,input().split())
a=[int(o) for o in input().split()]
ans=[0]*n
j=0
pi=-1
sa=sum(a)
cs=0
flag=0
i=0
while i<n:
    if i-pi==d or sa-cs==(n-i):
        if j>=m:
            flag=1
            break
        k=0
        while k<a[j]:
            ans[i]=j+1
            i+=1
            k+=1
        cs+=a[j]
        pi=i-1
        j+=1

    else:
        i+=1
if flag==0:
    print("YES")
    print(*ans)
else:
    print("NO")