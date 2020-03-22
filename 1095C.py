import heapq
def block(x): 
      
    v = [] 
    d=[]
    # Converting the decimal number 
    # into its binary equivalent. 
    
    while (x > 0): 
        v.append(int(x % 2)) 
        x = int(x / 2) 
  
    # Displaying the output when 
    # the bit is '1' in binary 
    # equivalent of number. 
    for i in range(0, len(v)): 
        if (v[i] == 1): 
            d.append(2**i)
            
            
    return d
n,k=map(int,input().split())
u=block(n)
lu=len(u)
for i in range(lu):
    u[i]=-u[i]
heapq.heapify(u)

if len(u)>k:
    print("NO")
else:
    while True:

        if lu==k:
            print("YES")
            for i in range(len(u)):
                print(-u[i],end=" ")
            print()
            break
        else:
            h=heapq.heappop(u)
            
            if h!=-1:
                heapq.heappush(u,h//2)
                heapq.heappush(u,h//2)
                lu+=1
            else:
                print("NO")
                break