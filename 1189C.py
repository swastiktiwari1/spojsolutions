n=int(input())
s=list(map(int,input().split()))
ps=[0]*(n+1)
for i in range(1,n+1):
    ps[i]=ps[i-1]+s[i-1]
#print(ps)
q=int(input())
for i in range(q):
    a,b=map(int,input().split())
    k=(ps[b]-ps[a-1])
   # print(k)
    if k>=10:
        print ((ps[b]-ps[a-1])//10)
    else:
        print("0")