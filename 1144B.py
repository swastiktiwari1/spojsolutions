n = int(input())
l = list(map(int, input().split()))
 
l.sort(reverse=True)
even = []; odd = []
for i in range(n):
    if l[i]%2 !=0:
        odd.append(l[i])
    else:
        even.append(l[i])
d = min(len(odd), len(even))
if d == len(odd):
    
    e = sum(even[d+1:])
else:
    e = sum(odd[d+1:])
if abs(len(even)-len(odd)) <= 1:
    print(0)
else:
    print(e)