from collections import Counter
n,k=map(int,input().split())
a=[int(o) for o in input().split()]
for i in range(n):
    a[i]=a[i]%(k)
d=dict(Counter(a))
#print(d)
ans=0
try:
    ans+=(d[0]//2)
except:
    ans+=0
for i in d.keys():
    j=k-i
    
   # print(ans)
    if i!=0:
        if i!=j:
            try:
                ans+=min(d[i],d[j])

                d[i]=0
            except:
                ans+=0
        else:
            ans+=(min(d[i],d[j])//2)
           # print("mij",min(d[i],d[j]))
            d[i]=0
       # print("ams",ans,i)
print(ans*2)