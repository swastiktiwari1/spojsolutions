import math
n=input()
n=int(n,base=2)
if n<=1:
    print(0)
else:
    print(math.ceil(math.log(n,4)))