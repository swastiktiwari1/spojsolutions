import math  
  
# method to print the divisors 
def printDivisors(n) : 
     lol=[]
    # Note that this loop runs till square root 
     i = 1
     while i <= math.sqrt(n): 
           
         if (n % i == 0) : 
               
            # If divisors are equal, print only one 
             if (n / i == i) : 
                lol.append(i) 
                
             else : 
                # Otherwise print both 
                 lol.append(i)
                 lol.append(n/i) 
         i = i + 1
     return(lol)
n=int(input())
a=[int(o) for o in input().split()]
a=sorted(a)
d=[]
sa=sum(a)
sa1=sa
d.append(sum(a))
aa=a[:]
for i in range(1,n):
    u=printDivisors(a[i])
    for j in u:
        sa+=(a[0]*j-a[0])
        sa-=(a[i]-a[i]//j)
        d.append(sa)
        sa=sa1
#print(d)
print(int(min(d)))