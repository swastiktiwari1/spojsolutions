import math
for _ in range(int(input())):
    n=int(input())
    s=set()
    a=[]
    su=0
    n1=n
    while su<n1:
        try:
            k=math.log(n,3)
            k1=int(k)
            k2=int(math.ceil(k))
            cc=3**k2
            if cc not in s:
                a.append(su+cc)
    
            lol=3**k1
            #print("lol",lol,su)
            if lol not in s:
               # print("andar")
                s.add(lol)
                su+=lol
                if su>=n1:
                    a.append(su)
                    break
                n-=lol
            else:
               # print("su",su)
                break
        except:
            break
    print(min(a))