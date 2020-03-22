from collections import Counter
from math import gcd  
  
# Function to reduce a fraction  
# to its lowest form 
def reduceFraction(x, y) : 
      
    d = gcd(x, y); 
  
    x = x // d; 
    y = y // d; 
    if x<0 and y<0:
        x=-x 
        y=-y
    elif y<0:
        x=-x
        y=-y
    return(str(x)+"/"+str(y)); 
n=int(input())
a=[int(o) for o in input().split()]
b=[int(o) for o in input().split()]
c=[0]*n
lolans=0
for i in range(n):
    if a[i]!=0:
        c[i]=str(reduceFraction(-b[i],a[i]))
    elif a[i]==0 and b[i]==0:
        lolans+=1
        c[i]="lol"
    else:
        c[i]="lol"
d=dict(Counter(c))
#print(d)
ma=0
for i in d.keys():
    if i!="lol":
        ma=max(d[i],ma)
print(ma+lolans)