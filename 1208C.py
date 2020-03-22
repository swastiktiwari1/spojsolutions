n=int(input())
i1=0
j1=1
ans=[]
for i in range(n):
    for j in range(n):
        
        if (i%2)==0:
            print(i1,end=" ")
            if j==2:
                ans.append(i1)
            i1+=2
        else:
            print(j1,end=" ")
            if j==1:
                ans.append(j1)
            j1+=2
    print()