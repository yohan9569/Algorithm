# 수학 / 브론즈 3 / 홀수

l = [i for i in map(int,open(0)) if i%2]
print(*[sum(l),min(l)] if l else [-1])  # else [-1] 에도 unpacking 적용됨.
