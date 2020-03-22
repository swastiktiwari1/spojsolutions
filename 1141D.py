n=int(raw_input())
a=raw_input()
b=raw_input()
a=list(a)
b=list(b)
lun=[None]*27
lun1=[None]*27
dow=[0]*n
dd=[0]*n
for i in range(27):
    lun[i]=[]
    lun1[i]=[]
for i in range(n):
    if a[i]=="?":
        lun[26].append(i+1)
        dow[i]=9
    else:
        lun[ord(a[i])-97].append(i+1)
    if b[i]=="?":
        lun1[26].append(i+1)
        dd[i]=9
    else:
        lun1[ord(b[i])-97].append(i+1)
d=[]

for i in range(26):
    for j in range(min(len(lun[i]),len(lun1[i]))):
        d.append([lun[i][j],lun1[i][j]])
        dow[lun[i][j]-1]=1
        dd[lun1[i][j]-1]=1
llun=len(lun[26])
flag=0
k=0
if k<(llun):
    for i in range(n):
        if dd[i]==0:
            d.append([lun[26][k],i+1])
            dow[lun[26][k]-1]=1
            dd[i]=1
            k+=1
            if k==llun:
                flag=1
                break
    i=0
    if flag==0:
        for i in range(n):
            if dd[i]==9:
                d.append([lun[26][k],i+1])
                dow[lun[26][k]-1]=1
                dd[i]=1
                k+=1
                if k==llun:
                    i+=1
                    flag=2
                    break


ll1=len(lun1[26])
if flag==2:
    if i<ll1:
        for j in range(n):
            if dow[j]!=1:
                d.append([j+1,lun1[26][i]])
                dow[j]=1
                dd[lun1[26][i]-1]=1
                i+=1
                if i==ll1:
                    break
else:
    i=0
    if i<ll1:
        for j in range(n):
            if dow[j]!=1:
                d.append([j+1,lun1[26][i]])
                dow[j]=1
                dd[lun1[26][i]-1]=1
                i+=1
                if i==ll1:
                    break
    
#print(dow)       

print(len(d))
for i in range(len(d)):
    print d[i][0],d[i][1]