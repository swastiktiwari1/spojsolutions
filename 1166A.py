import math
def binomialCoef(n, k): 
    C = [[0 for x in range(k+1)] for x in range(n+1)] 
  
    # Calculate value of Binomial Coefficient in bottom up manner 
    for i in range(n+1): 
        for j in range(min(i, k)+1): 
            # Base Cases 
            if j == 0 or j == i: 
                C[i][j] = 1
  
            # Calculate value using previously stored values 
            else: 
                C[i][j] = C[i-1][j-1] + C[i-1][j] 
  
    return C[n][k] 
n=int(input())
a=[None]*n
d=dict()
for i in range(n):
    a[i]=input()
    a=list(a)
    try:
        d[a[i][0]]+=1
    except:
        d[a[i][0]]=1
mp=0
for i in d.values():
    
    mp+=binomialCoef(int(math.ceil(i/2)),2)
    mp+=binomialCoef(int(math.floor(i/2)),2)

        
print(mp)