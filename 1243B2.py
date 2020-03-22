for _ in range(int(input())):
    n=int(input())
    a=list(input())
    b=list(input())
    ans=[]
    d1=dict()
    d2=dict()
    for i in range(n):
        try:
            d1[a[i]].add(i)
        except:
            d1[a[i]]=set([(i)])
        try:
            d2[b[i]].add(i)
        except:
            d2[b[i]]=set([i])
   # print(d1)
    f1=0
    for i in range(n):
        d1[a[i]].remove(i)
        d2[b[i]].remove(i)
        if a[i]!=b[i]:
            flag=0
            for j in d1[a[i]]:
                if a[j]!=b[j] :
                    ans.append([j+1,i+1])
                    d1[a[j]].remove(j)
                    a[j],b[i]=b[i],a[j]
                    try:
                        d1[a[j]].add(j)
                    except:
                        d1[a[j]]=set([(j)])
                    try:
                        d2[b[j]].add(j)
                    except:
                        d2[b[j]]=set([j])
                    flag=1
                    break
            if flag==0:
                if a[i] in d2:
                    for j in d2[a[i]]:
                        if a[j]!=b[j]:
                            ans.append([j+1,j+1])
                            d1[a[j]].remove(j)
                            d2[b[j]].remove(j)
                            a[j],b[j]=b[j],a[j]
                         #   print(a,b)
                            try:
                                d1[a[j]].add(j)
                            except:
                                d1[a[j]]=set([(j)])
                            try:
                                d2[b[j]].add(j)
                            except:
                                d2[b[j]]=set([j])
                            d1[a[j]].remove(j)
                            ans.append([j+1,i+1])
                            a[j],b[i]=b[i],a[j]
                           # print(i,j,a,b)
                            try:
                                d1[a[j]].add(j)
                            except:
                                d1[a[j]]=set([(j)])
                            try:
                                d2[b[j]].add(j)
                            except:
                                d2[b[j]]=set([j])
                            flag=1
                            break
            if flag==0:
                f1=1
                break
    if f1==0:
        print("Yes")
        print(len(ans))
        for i in ans:
            print(*i)
    else:
        print("No")
       # print(a)
       # print(b)