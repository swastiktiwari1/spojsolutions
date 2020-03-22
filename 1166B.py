k=int(input())
f,s=0,0
flag=0
for i in range(5,k):
    if k%i==0:
        if k//i>=5:
            f=k//i
            s=i
            flag=1
            break
if flag==0:
    print("-1")
else:
    ans=[[0 for i in range(f)]for j in range(s)]
    st="aeiou"
    d={'a':0,'e':1,'i':2,'o':3,'u':4}
    for i in range(5):
        ans[0][i]=st[i]
        ans[i][0]=st[i]
    for i in  range(s):
        for j in range(f):
            if ans[i][j]==0:
                if i>0:
                    jj=d[ans[i-1][j]]
                    jj=(jj+1)%5
                    ans[i][j]=st[jj]
                else:
                    jj=d[ans[i][j-1]]
                    jj=(jj+1)%5
                    ans[i][j]=st[jj]
        print("".join(ans[i]),end="")