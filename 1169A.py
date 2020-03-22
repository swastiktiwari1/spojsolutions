n,a,x,b,y=map(int,input().split())
flag=False
a-=1
b-=1
x-=1
y-=1
while a!=x and b!=y:
    if a==b:
        flag=True
        break
    
    a=((a+1)%(n))
    b=((b-1)%(n))
   # print(a+1,b+1)
    if a==b:
        flag=True
        break
    
    
print("YES" if flag==True else "NO")