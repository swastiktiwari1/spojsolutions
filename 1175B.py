x=(2**32)-1
n=int(input())
st=[0]
fs=[]
flag=0
for i in range(n):
    s=[o for o in input().split()]
    if s[0]=="add":
        k=st.pop()
        k+=1
        st.append(k)
    elif s[0]=="for":
        st.append("(")
        st.append(0)
        fs.append(int(s[1]))
    else:
        a=0
        while st[-1]!="(":
            a+=st.pop()
        st.pop()
        lol=fs.pop()*a
        if lol>x:
            flag=1
            break
        st.append(lol)
    
d=0
if flag==0:
    while st:
        d+=st.pop() 
        if d>x:
            flag=1
            break
print(d if flag==0 else "OVERFLOW!!!")