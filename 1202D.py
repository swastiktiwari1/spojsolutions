import bisect
ans=[-1]
n=0
while ans[-1]<=1000000000:
    ans.append(n*(n+1)//2 )
    #print(ans[-1])
    n+=1
ans.pop(0)
#print(ans[:10])
for _ in range(int(input())):
    n=int(input())
    s="1"
    lol=bisect.bisect(ans,n)
    s+="3"*(lol)
   # print(s)
    bacha=(n-ans[lol-1])
    s=list(s)
    s.pop()
    s.pop()
    s.append("1"*bacha)
    s.append("337")
    print(("".join(s)))