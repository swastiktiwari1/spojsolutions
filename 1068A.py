n,m,k,l=map(int,input().split())
kitne=(k+l-1)//m+1
print(kitne if kitne*m<=n else "-1")