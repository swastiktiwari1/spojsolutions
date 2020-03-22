n=int(input())
if n<2:
    print("0")
elif n%2!=0:
    print("0")
else:
    print(2**(n//2))