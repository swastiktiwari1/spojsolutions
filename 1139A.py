en=list("02468")
n=int(input())
s=input()
ans=0
for i in range(n):
    if s[i] in en:
        ans+=(i+1)
print(ans)