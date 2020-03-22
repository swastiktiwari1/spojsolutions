n=int(input())
a=[int(o) for o in input().split()]
ans=[]
for i in range(1,101):
    su=0
    for j in range(n):
        su+=min(abs(i-a[j]),abs(i+1-a[j]),abs(i-1-a[j]))
    ans.append([su,i])
lol=min(ans[:])
print(*lol[::-1])