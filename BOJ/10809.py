# 구현 / 브론즈 2 / 알파벳 찾기

S = input()
apb = list('abcdefghijklmnopqrstuvwxyz')
print(' '.join([ str(S.find(i)) for i in apb]))
