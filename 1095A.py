l=int(input())
s=input()
n=2
j=0
while j<=l:
    j=(n-1)*(n-2)//2+1
    if j>l:
        break
    print(s[j-1],end="")
    n+=1