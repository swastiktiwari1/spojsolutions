from collections import Counter
n=int(input())
a=[int(o) for o in input().split()]
u=list(set(a))
c=dict(Counter(a))
cm=[0]*(n**2)
lu=len(u)
pk=0
for i in range(lu):
    #print(u[i])
    cm[i]=[u[i],c[u[i]]]
    #print(cm)
if n%2==0:
    flag=0
    for i in range(lu):
        if (cm[i][1])%4!=0:
            flag=1
    if flag==1:
        print("NO")
    else:
        k=0
        matr=[[0 for i in range(n)] for j in range(n)]
        for i in range(n//2):
            for j in range(n//2):
                matr[i][j]=cm[k][0]
                matr[i][n-1-j]=cm[k][0]
                matr[n-1-i][j]=cm[k][0]
                matr[n-1-i][n-1-j]=cm[k][0]
                cm[k][1]-=4
                if cm[k][1]==0:
                    k+=1
        print("YES")
        for i in range(n):
            
            print(*matr[i])
else:
    fp=[]
    tp=[]
    op=[]
    for i in range(lu):
        if cm[i][1]>=4:
            fp.append([cm[i][0],4*(cm[i][1]//4)])
            cm[i][1]=(cm[i][1])%4
        if cm[i][1]>=2:
            tp.append([cm[i][0],2*(cm[i][1]//2)])
            cm[i][1]=(cm[i][1])%2
        if cm[i][1]>=1:
            op.append([cm[i][0],1*(cm[i][1]//1)])
            cm[i][1]=(cm[i][1])%1
    if len(op)>1:
        flag=1
    try:
        flag=0
        k=0
        matr=[[0 for i in range(n)] for j in range(n)]
        for i in range(n//2):
            for j in range(n//2):
                matr[i][j]=fp[k][0]
                matr[i][n-1-j]=fp[k][0]
                matr[n-1-i][j]=fp[k][0]
                matr[n-1-i][n-1-j]=fp[k][0]
                fp[k][1]-=4
                if fp[k][1]==0:
                    k+=1
    except:
        flag=1
    if flag==0:
        try:
            
            loll=n//2
            for i in range(n//2):
                matr[loll][i]=fp[k][0]
                matr[loll][n-1-i]=fp[k][0]
                fp[k][1]-=2
                if fp[k][1]==0:
                    k+=1
        except:
            try:
                k=0
                for j in range(i,n//2):
                    matr[loll][j]=tp[k][0]
                    matr[loll][n-1-j]=tp[k][0]
                    tp[k][1]-=2
                    if tp[k][1]==0:
                        k+=1
                pk=k
            except:
                flag=1
        try:
            if pk==0:
                loll=n//2
                #print("dfnkj")
                for i in range(n//2):
                    matr[i][loll]=fp[k][0]
                    matr[n-1-i][loll]=fp[k][0]
                    fp[k][1]-=2
                    if fp[k][1]==0:
                        k+=1
            else:
                k=pk
                try:
                
                    for j in range(i,n//2):
                        matr[j][loll]=tp[k][0]
                        matr[n-1-j][loll]=tp[k][0]
                        tp[k][1]-=2
                        if tp[k][1]==0:
                            k+=1
                except:
                    
                    flag=1
        except:
            try:
                k=0
                for j in range(i,n//2):
                    matr[j][loll]=tp[k][0]
                    matr[n-1-j][loll]=tp[k][0]
                    tp[k][1]-=2
                    if tp[k][1]==0:
                        k+=1
            except:
                
                flag=1
    if flag==0:
        yoyo=op[0][0]
        matr[n//2][n//2]=yoyo
    #print(matr[n//2][n//2])
        print("YES")
        for i in range(n):
            print(*matr[i])
    else:
        print("NO")