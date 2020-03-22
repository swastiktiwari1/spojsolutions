for _ in range(int(input())):
    a,b=map(int,input().split())
    if b<a:
        a,b=b,a
    b-=a
    i=0
    while True:
        lol=(i*(i+1))//2
        z=(lol+b)/2
        x=lol-z
        if(z==int(z)):
            if (z>=0  and x>=0 ):
               # print(z,x)
                print(i)
                break
        i+=1