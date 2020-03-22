s=input()
d=input()
s0=int(ord(s[0])-96)
s1=int(s[1])
d1=int(d[1])
d0=int(ord(d[0])-96)
em=min(abs(s0-d0),abs(s1-d1))
tm=(min(abs(s0-d0),abs(s1-d1))+abs(abs(s0-d0)-abs(s1-d1)))
print(tm)
if s0>d0:
    k=["L"]
else:
    k=["R"]
if s1>d1:
    k.append("D")
else:
    k.append("U")
for i in range(em):
    print("".join(k))
if abs(s0-d0)>abs(s1-d1):
    if s0>d0:
        g="L"
    else:
        g="R"
else:
    if s1>d1:
        g="D"
    else:
        g="U"
for i in range(tm-em):
    print(g)