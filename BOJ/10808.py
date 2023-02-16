# 문자열 / 브론즈 4 / 알파벳 개수


from collections import Counter

a = 'abcdefghijklmnopqrstuvwxyz'
c = Counter(input())

print(' '.join(str(c[s]) for s in a))
# another way
# print(*[c[s] for s in a])
