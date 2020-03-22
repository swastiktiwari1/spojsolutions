for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=""
    flag=0
    # s=0
    for i in s:
        if int(i)%2==1:
            ans+=i
            flag+=1
            if flag==2:
                break
    if flag==2:
        print(ans)
    else:
        print("-1")