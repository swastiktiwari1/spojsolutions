n=int(input())
s1=input()
s2=input()
first=[]
second=[]
none=[]
both=[]
for i in range(n):
    if s1[i]=="1" and s2[i]=="0":
        first.append(i+1)
    elif s1[i]=="0" and s2[i]=="1":
        second.append(i+1)
    elif s1[i]=="1" and s2[i]=="1":
        both.append(i+1)
    else:
        none.append(i+1)
fl=len(first)
sl=len(second)
bl=len(both)
nl=len(none)
ans=[]
flag=0
for a in range(fl+1):
    for c in range(bl+1):
        b=(a+c)-(bl-c)
        if b<=sl and b>=0 and a+c+(sl-b)<=(n//2) and b+(bl-c)==a+c:
          #  print(b+(bl-c),a,c)
            ans=[a,sl-b,c,n//2-(a+c+(sl-b))]
            if ans[3]<=nl and ans[3]>=0:
              #  print(ans)
                flag=1
                break
    if flag==1:
        break
if flag==1:
    #print(ans)
    print(*first[:ans[0]],*second[:ans[1]],*both[:ans[2]],*none[:ans[3]])

else:
    print("-1")