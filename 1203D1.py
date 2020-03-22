def f(n):
    for i in range(-1,lt):
        if right[i+1]-left[i]>n:
            return True
    return False
s=input()
t=input()
ls=len(s)
lt=len(t)
right=dict()
left=dict()
i=0
j=0
ls=len(s)
left[-1]=-1
while i<lt:
    if s[j]==t[i]:
        left[i]=j
        i+=1
    j+=1
j=ls-1
i=lt-1
right[lt]=ls
while i>=0:
    if s[j]==t[i]:
        right[i]=j
        i-=1
    j-=1
low=0
high=ls-1
#print(right,"\n",left)
while low<=high:
    mid=(high+low)//2
  #  print(mid,f(mid))
    if f(mid):
        low=mid+1
    else:
        high=mid-1
print(high)