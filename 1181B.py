import math
l=int(input())
n=input()
if n.count("0")==l-1:
    print(n)
else:
    if l%2==0:
        a=l//2
        b=l//2
    else:
    
        a=int(math.floor(l/2))
        b=int(math.ceil(l/2))
        
    while a!=-1 and n[a]=="0":
            a-=1
    while b!=l and n[b]=="0":
            b+=1
    st1=(l+1)*"0"+n[:a]
    st2=(l+1)*"0"+n[a:]
    st3=(l+1)*"0"+n[:b]
    st4=(l+1)*"0"+n[b:]
  #  print(st1,st2)
   # print(st3,st4)
    
    
    mlab=max(len(st1),len(st2))-1
    mlba=max(len(st3),len(st4))-1
    d=["0"]*(l+1)
    c=0
    i=-1
    while i>=-(l+1):
        u=str(int(st1[i])+int(st2[i])+c)
       # print(u)
        if len(u)>1:
            c=int(u[0])
            k=u[1]
            d[i]=str(u[1])
        else:
            d[i]=str(u)
            c=0
        i-=1
    d1=[0]*(l+1)
    i=-1
    c=0
    while i>=-l:
        u=str(int(st3[i])+int(st4[i])+c)
        if len(u)>1:
            c=int(u[0])
            k=u[1]
            d1[i]=str(u[1])
        else:
            d1[i]=str(u)
            c=0
        i-=1
   # print(d,d1)
    while d[0]==0 or d[0]=="0" :
        d.pop(0)
    while d1[0]==0 or d1[0]=="0" :
        d1.pop(0)
    if len(d)>len(d1):
        print("".join(d1))
    elif len(d1)>len(d):
        print("".join(d))
    else:
        res=0
        for i in range(len(d)):
            if d[i]<d1[i]:
                res=0
                break
            elif d1[i]<d[i]:
                res=1
                break
        if res==1:
            print("".join(d1))
        else:
            print("".join(d))