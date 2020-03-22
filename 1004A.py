# cook your dish here
n,d=input().split()
n=int(n)
d=int(d)
a=[int(n) for n in input().split()]
o=[]
r=0
for i in range(len(a)-1):
    o.append(a[i+1]-a[i])
  
for j in range(len(o)):
    if o[j]>(2*d):
        r+=2
    elif o[j]==(2*d):
        r+=1
    
print(r+2)