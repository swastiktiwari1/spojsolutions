n,k=map(int,input().split())
a=[int(o) for o in input().split()]
d=[]
a=sorted(a)

lol=n//2
i=n//2
cv=a[lol]
#print(a)
while i<n:
    try:
        d.append([d[-1][0]+(a[i]-cv)*(i-lol),a[i],i])
    except:
        d.append([(a[i]-cv)*(i-lol),a[i],i])
    #print(d)
    cv=a[i]
    if d[-1][0]>k:
        ans=d[-2][1]+(k-d[-2][0])//(d[-2][2]-lol+1)
        break
    if i==n-1:
        ans=d[-1][1]+(k-d[-1][0])//(d[-1][2]-lol+1)
        break
    i+=1
#print(d)
print(ans)