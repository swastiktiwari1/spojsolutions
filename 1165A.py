n,x,y=map(int,input().split())
s=input()
s=list(s)
s=s[::-1]
i=1
op=0
for i in range(y):
    if s[i]=="1":
        op+=1
        s[i]="0"
if s[y]=="0":
    s[y]="1"
    op+=1
for i in range(y+1,x):
    if s[i]=="1":
        op+=1
        s[i]="0"
s=s[::-1]
print(op)