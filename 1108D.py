n=int(input())
s=input()

s=list(s)
arr=[s[0]]
count=0
for i in range(1,n):
    if arr[i-1]!=s[i]:
        arr.append(s[i])
    else:
        count+=1
        if i<n-1:
            if s[i]=="G" and s[i+1]=="R":
                arr.append("B")
            elif s[i]=="G" and s[i+1]=="B":
                arr.append("R")
            elif s[i]=="G" and s[i+1]=="G":
                arr.append("B")
            elif s[i]=="R" and s[i+1]=="G":
                arr.append("B")
            elif s[i]=="R" and s[i+1]=="B":
                arr.append("G")
            elif s[i]=="R" and s[i+1]=="R":
                arr.append("B")
            elif s[i]=="B" and s[i+1]=="G":
                arr.append("R")
            elif s[i]=="B" and s[i+1]=="R":
                arr.append("G")
            else:
                arr.append("G")
        else:
            if s[i]=="R" or s[i]=="G":
                arr.append("B")
            else:
                arr.append("R")
print(count)
print("".join(arr))