import heapq
n=int(input())
s1=set()
s2=set()
h1=[]
h2=[]
a=[int(o) for o in input().split()]
lol=[]
for i in range(n):
    if a[i] not in s1:
        s1.add(a[i])
        h1.append([i,a[i]])
for i in range(n-1,-1,-1):
    if a[i] not in s2:
        s2.add(a[i])
        h2.append([i,a[i]])
if h1[0][1]!=h2[0][1]:
    lol.append(h2[0][0]-h1[0][0])
if h1[1][1]!=h2[0][1]:
    lol.append(h2[0][0]-h1[1][0])
if h1[0][1]!=h2[1][1]:
    lol.append(h2[1][0]-h1[0][0])
if h1[1][1]!=h2[1][1]:
    lol.append(h2[1][0]-h1[1][0])
print(max(lol))