n=int(input())
i=1
ans=0
while True:
    lol=int(bin(i)[2:])
    if lol<=n:
        ans+=1
    else:
        break
    i+=1
print(ans)