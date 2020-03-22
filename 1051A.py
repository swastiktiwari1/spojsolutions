# cook your dish here
T=int(input())
while T>0:
    s=input()
    count1 = 0
    count2 = 0
    count3 = 0
    nums=[]
    caps=[]
    sms=[]
    for a in s: 
    # Checking for lowercase letter and converting to uppercase. 
        if (a.isupper()) == True: 
            count1+= 1
            caps.append(a)
    # Checking for uppercase letter and converting to lowercase. 
        elif (a.islower()) == True: 
            count2+= 1
            sms.append(a)
    # Checking for whitespace letter and adding it to the new string as it is. 
        elif (a.isdigit()) == True: 
            count3+= 1
            nums.append(a)
    s=list(s)
    if count3>=1 and count2>=1 and count1>=1:
        print("".join(s))
    elif count1>=1 and count2>=1:
        if count2>=2:
            s[s.index(sms[0])]="1"
        else:
            s[s.index(caps[0])]="1"
        print("".join(s))
    elif count2>=1 and count3>=1:
        if count2>=2:
            s[s.index(sms[0])]="A"
        else:
            s[s.index(nums[0])]="A"
        print("".join(s))
    elif count1>=1 and count3>=1:
        if count1>=2:
            s[s.index(caps[0])]="a"
        else:
            s[s.index(nums[0])]="a"
        print("".join(s))
    elif count1>=1:
        s[0]="a"
        s[1]="1"
        print("".join(s))
    elif count2>=1:
        s[0]="A"
        s[1]="1"
        print("".join(s))
    elif count3>=1:
        s[0]="a"
        s[1]="A"
        print("".join(s))
        
        
    T-=1