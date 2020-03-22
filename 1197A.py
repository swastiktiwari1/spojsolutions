for _ in range(int(input())):
    n=int(input())
    a=[int(o) for o in input().split()]
    a=sorted(a)
    print(min(n-2,a[-2]-1))