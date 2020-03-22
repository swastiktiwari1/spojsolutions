for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    s=list(s)
    lol=0
    ans=[]
    for i in range(n):
       # print(k,s[i])
        if s[i]=="1":
            lol+=1
        elif s[i]=="0":
            if k>=lol:
                k-=(lol)
                s[i]=-1
                ans.append("0")
            else:
                for j in range(n):
                    if s[j]!=-1:
                        ans.append(s[j])
                        s[j]=-1
                ans[i],ans[i-k]=ans[i-k],ans[i]
                k=0
    for i in range(n):
        if s[i]!=-1:
            ans.append(s[i])
            s[i]=-1
    print("".join(ans))