# 수학 / 브론즈 1 / 초콜릿 자르기

a, b = map(int, input().split())
m, n = max(a,b), min(a,b)-1
print(m-1 + n*m)
