n=input()
for i in range(1000000):
    
    st=0
    for j in str(int(n)+i):
        st+=int(j)
    if st%4==0:
        print(int(n)+i)
        break