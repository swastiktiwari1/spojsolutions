N = int(input())
 
s = input()
 
res = 999999
for i in range(N-3):
    A = s[i]
    B = s[i+1]
    C = s[i+2]
    D = s[i+3]
    
    d1 = ord(A)-ord('A')
    if d1<0:
        d1 += 26
        
    d2 = ord(B)-ord('C')
    if d2<0:
        d2 += 26
        
    d3 = ord(C)-ord('T')
    if d3<0:
        d3 += 26
        
    d4 = ord(D)-ord('G')
    if d4<0:
        d4 += 26
    
    #print(d1,d2,d3,d4)
    diff = min(d1,26-d1) + min(d2,26-d2) + min(d3,26-d3) + min(d4,26-d4)
    
    res = min(res,diff)
    
print(res)