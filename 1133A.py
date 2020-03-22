h1,m1=map(int,input().split(":"))
h2,m2=map(int,input().split(":"))
t1=h1*60+m1
t2=h2*60+m2
t3=(t1+t2)//2
s1="00"+str(t3//60)
s2="00"+str(t3%60)
print(s1[-2]+s1[-1]+":"+s2[-2]+s2[-1])