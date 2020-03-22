l,r=map(int,input().split())
flag=-1
for i in range(l,r+1):
    if len(list(str(i)))==len(set(list(str(i)))):
        flag=i
        break
print(flag)