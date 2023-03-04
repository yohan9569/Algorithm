# 문자열 / 브론즈 2 / 너의 이름은 몇 점이니?


d = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
a = 0
input()

for s in input():
    a += d[s]

print(a)


# another way - ord 활용 방식 배웠다.
a=input;a();print(sum(ord(x)-64 for x in a()))
