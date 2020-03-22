n=int(input())
A=0
B=0
count=1
while n:
    a,b=map(int,input().split())
    if(A==B):count+=min(a-A,b-B)
    elif(A>B):
        if(b>=A):
            count+=min(a-A,b-A)+1
    else:
        if(a>=B):
            count+=min(a-B,b-B)+1
    A=a
    B=b
    n-=1
print(count)