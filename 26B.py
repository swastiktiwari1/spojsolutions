s=input()
ml=0
l=0
r=0
for i in range(len(s)):
    if s[i]=="(":
        l+=1
    else:
        if l>r:
            r+=1
            ml=max(ml,r)
print(2*r)