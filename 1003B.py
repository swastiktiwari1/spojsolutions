a,b,x=map(int,input().split())
x-=1
lis=["0","1"]
a-=1
b-=1
while x!=0:
    if a>0 and lis[-1]=="1":
        lis.append("0")
        x-=1
        a-=1
    elif a>0 and lis[0]=="1":
        lis=["0"]+lis
        x-=1
        a-=1
    elif b>0 and lis[-1]=="0":
        lis.append("1")
        x-=1
        b-=1
    elif b>0 and lis[0]=="0":
        lis=["1"]+lis
        b-=1
        x-=1
if a>0:
    x=lis.index("0")
    lol=["0"]*(a+1)
    lis[x]="".join(lol)
if b>0:
    x=lis.index("1")
    lol=["1"]*(b+1)
    lis[x]="".join(lol)
print("".join(lis))