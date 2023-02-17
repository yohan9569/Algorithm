# 문자열 / 브론즈 1 / 팰린드롬수


while 1:
    n = input()
    if n == '0':
        break

    l = len(n)//2
    if n[:l] == n[:-l-1:-1]:
        print('yes')
    else:
        print('no')
