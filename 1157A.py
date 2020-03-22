def func(x):
    x+=1
    while x%10==0:
        x//=10
    return x
a=set()
n=int(raw_input())
while (not (n in a)):
    a.add(n)
    n=func(n)
print len(a)