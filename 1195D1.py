n=int(raw_input())
ans=[0]*30
lol=[o for o in raw_input().split()]
for i in range(n):
        lol[i]=lol[i][::-1]
        for j in range(len(lol[i])):
                ans[2*j]+= (int(lol[i][j])*n) 
                ans[2*j+1]+= (int(lol[i][j])*n) 
#print(ans)
realans=[0]*30
c=0
for i in range(30):
        realans[i]=str((ans[i]+c)%10)
        c=((ans[i]+c)//10)
print((int("".join(realans[::-1])))%998244353)