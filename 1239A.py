f=[1]*(100005)
for i in range(2,100005):
    f[i]=f[i-1]+f[i-2]
n,m=map(int,input().split())
print((2*(f[n]+f[m]-1))%1000000007)