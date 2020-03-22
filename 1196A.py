for _ in range(int(input())):
    a=[int(o) for o in input().split()]
    a=sorted(a)
    print(sum(a)//2)