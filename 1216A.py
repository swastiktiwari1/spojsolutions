n=int(input())
s=list(input())
ac=0
bc=0
cc=0
for i in range(n):
    if s[i]=="a":
        ac+=1
    elif s[i]=="b":
        bc+=1
    if (i+1)%2==0:
        if ac>bc:
            s[i]="b"
            cc+=1
            ac-=1
            bc+=1
        elif bc>ac:
            s[i]="a"
            cc+=1
            bc-=1
            ac+=1
print(cc)
print("".join(s))