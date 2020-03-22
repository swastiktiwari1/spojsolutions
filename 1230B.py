n, k = map(int, input().split())
s = [*input()]
if k != 0:
    if n == 1: s[0] = '0'
    elif s[0] != '1': k, s[0] = k - 1, '1'
    for i in range(1, n): 
        if k <= 0: break
        if s[i] != '0': k, s[i] = k - 1, '0'
print(''.join(s))