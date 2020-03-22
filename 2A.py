d=dict()
p=0
w=0
l=[]
for _ in range(int(input())):
    a,b=input().split()
    l.append([a,b])
    try:
        d[a]+=int(b)
    except:
        d[a]=int(b)
win=[]
m=0
for i in d.keys():
    if d[i]>m:
        m=d[i]
for i in d.keys():
    if d[i]==m:
        win.append(i)

f=dict()
for i in range(len(l)):
    a,b=l[i][0],l[i][1]
    try:
        f[a]+=int(b)
    except:
        f[a]=int(b)
    if f[a]>=m:
        if a in win:
            #print(w)
            w=a
            break
        
print(w)