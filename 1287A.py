for  _ in range(int(input())):
    n=int(input())
    s=input()
    lol=list(s.split("A"))
    # print(lol)
    lol.pop(0)
    curr=0
    for i in lol:
        curr=max(len(i),curr)
    print(curr)