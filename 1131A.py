w1,h1,w2,h2=map(int,input().split())
s=w1+w2+2*h1+2*h2+4
lol=abs(w1-w2)
print(s+lol)