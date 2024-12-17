n = int(input())
full = n*2
for i in range(1, full):
    if i > n:
        i = full - i
    print(' '*(n-i) + '*'*(2*i-1))