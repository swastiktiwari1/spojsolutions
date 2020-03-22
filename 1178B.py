s=input()
n=len(s)
s+="p"
pref=[0]*(n+1)
for i in range(1,n+1):
    pref[i]=pref[i-1]
    if s[i-1]=="v" and s[i]=="v":
        pref[i]+=1
ans=0
for i in range(n):
    if s[i]=="o":
        ans+=(pref[i+1]*(pref[n]-pref[i+1]))
print(ans)