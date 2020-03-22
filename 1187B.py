from collections import Counter
def f(h):
    for i in c.keys():
        kk=ord(i)-97
        if ard[h][kk]<c[i]:
            return False
    return True
    
n=int(raw_input())
s=raw_input()
m=int(raw_input())
ard=[None]*n
pc=[0]*26
for i in range(n):
    pc[ord(s[i])-97]+=1
    ard[i]=pc[:]
for i in range(m):
    a=raw_input()
    c=dict(Counter(a))
    low=len(a)-1
    high=n-1
    while high>=low:
        mid=(high+low)/2
        if f(mid)==False:
            low=mid+1
        else:
            high=mid-1
    print(low+1)