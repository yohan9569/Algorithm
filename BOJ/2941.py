# 구현 / 실버 5 / 크로아티아 알파벳


s = input()
cro=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in cro:
    s = s.replace(c, 'a')
print(len(s))
