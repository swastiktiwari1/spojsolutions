def f():
    n = int(input())
    o = sum(int(e) & 1 for e in input().split())
    return n - o, o
 
for _ in range(int(input())):
    e1, o1 = f()
    e2, o2 = f()
    print(e1 * e2 + o1 * o2)