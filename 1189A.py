n=int(input())
s=input()
cz=s.count("0")
co=s.count("1")
if co!=cz or n==1:
    print("1")
    print(s)
else:
    print("2")
    s=list(s)
    print("".join(s[:1]),"".join(s[1:]))