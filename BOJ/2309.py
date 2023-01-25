# 브루트포스, 정렬 / 브론즈 1 / 일곱 난쟁이


from itertools import combinations as cb

dwarfs = [*map(int, open(0))]

for c in cb(dwarfs, 7):
    if sum(c) == 100:
        print(*sorted(c))
        break
