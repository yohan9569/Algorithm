# 구현 / 브론즈 2 / 음계


In = input()

if In == '1 2 3 4 5 6 7 8': 
    ans = 'ascending'
elif In == '8 7 6 5 4 3 2 1':
    ans = 'descending'
else:
    ans = 'mixed'

print(ans)
