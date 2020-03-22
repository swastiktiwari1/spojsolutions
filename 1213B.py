
for _ in range(int(input())):
        n=int(input())
        a=[int(o) for o in input().split()]
        s=[]
        lis=[]
        for i in range(n):
            if not(s):
                s.append(a[i])
                continue
            while s and s[-1]>a[i]:
                lis.append(s.pop())
            s.append(a[i])
        print(len(lis))