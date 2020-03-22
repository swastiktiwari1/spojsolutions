import math
n=int(input())
yo=int(math.ceil(n/3))
s=input()
s=list(s)
fl=["R","G","B"]*yo
sl=["R","B","G"]*yo
tl=["G","R","B"]*yo
cl=["G","B","R"]*yo
pl=["B","R","G"]*yo
chl=["B","G","R"]*yo
fc=0
sc=0
tc=0
cc=0
pc=0
chc=0
for i in range(n):
    if fl[i]!=s[i]:
        fc+=1
    if sl[i]!=s[i]:
        sc+=1
    if tl[i]!=s[i]:
        tc+=1
    if cl[i]!=s[i]:
        cc+=1
    if pl[i]!=s[i]:
        pc+=1
    if chl[i]!=s[i]:
        chc+=1
zol=[fc,sc,tc,cc,pc,chc]
lol=min(zol)
ind=zol.index(lol)
if ind==0:
    print(fc)
    fl=fl[:n]
    print("".join(fl))
elif ind==1:
    print(sc)
    sl=sl[:n]
    print("".join(sl))
elif ind==2:
    print(tc)
    tl=tl[:n]
    print("".join(tl))
elif ind==3:
    print(cc)
    cl=cl[:n]
    print("".join(cl))
elif ind==4:
    print(pc)
    pl=pl[:n]
    print("".join(pl))
elif ind==5:
    print(chc)
    chl=chl[:n]
    print("".join(chl))