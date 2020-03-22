n=input()
ln=len(n)
if ln>1:
    k=["9"]*(ln-1)
    f=int("".join(k))
    f2=int(n)-f
    ans=9*len(k)
    f2=str(f2)
    for i in f2:
        ans+=int(i)
    print(ans)
else:
    print(n)