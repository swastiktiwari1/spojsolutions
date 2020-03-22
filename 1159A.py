n=int(raw_input())
s=raw_input()
ist=0
for i in range(n):
    if s[i]=="-":
        ist=max(ist-1,0)
    else:
        ist+=1
print(ist)