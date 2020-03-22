for _ in range(int(input())):
    a=input()
    b=input()
    b=b[::-1]
    a=a[::-1]
    lol=b.index("1")
    a=a[lol:]
    print(a.index("1"))