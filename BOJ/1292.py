# 수학 / 브론즈 1 / 쉽게 푸는 문제


a,b = map(int, input().split())
seq = [0]

for i in range(min(b+1, 46)):
    seq += [i] * i
    
print(sum(seq[a:b+1]))
