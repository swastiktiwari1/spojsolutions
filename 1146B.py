t = input()
n = len(t)
s1 = ''
last_index = -1
for i in range(n):
    if t[i] != 'a':
        s1 += t[i]
    else:
        last_index = i
if len(s1) % 2 or s1[:len(s1) // 2] != s1[len(s1) // 2:]:
    print(':(')
else:
    s = ''
    count = i = 0
    n1 = len(s1) // 2
    while count < n1:
        if t[i] != 'a':
            count += 1
        s += t[i]
        i += 1
    while i < n and i <= last_index:
        if t[i] == 'a':
            s += t[i]
            i += 1
        else:
            break
    if i >= last_index:
        print(s)
    else:
        print(':(')