n=int(input())
s=input()
s=list(s)
a=[int(o) for o in input().split()]
i=0
flag=0
while i<n and flag==0:
    if a[int(s[i])-1]>int(s[i]):
        flag=1
        while i<n and a[int(s[i])-1]>=int(s[i]):
            s[i]=str(a[int(s[i])-1])
            i+=1
    i+=1
print("".join(s))