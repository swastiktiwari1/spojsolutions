n=int(input())
a=input()
flag=0
for i in range(n-1):
    if ord(a[i])>ord(a[i+1]):
        flag=1
        print("YES")
        print(i+1,i+2)
        break
if flag==0:
    print("NO")