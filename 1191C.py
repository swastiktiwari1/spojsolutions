import math
n,m,k=map(int,input().split())
p=[int(o)-1 for o in input().split()]
p=sorted(p)
i=0
count=0
ans=0
while i<m:
    fi=(p[i]-count)//k*k
    #print(fi)
    tempc=0
    while i<m and p[i]<fi+k+count:
       # print(p[i],count)
        i+=1
        tempc+=1
    count+=tempc
    ans+=1
print(ans)