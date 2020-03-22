sieve=[0]*3005
sieve[1]=1
sieve[0]=1
for i in range(2,3005):
    if sieve[i]==0:
        j=i+i
        while j<3005:
            sieve[j]+=1
            j+=i
n=int(input())
ans=0
for i in range(1,n+1):
    if sieve[i]==2:
        ans+=1
print(ans)