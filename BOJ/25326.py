# 문자열 / 브론즈 1 / 다중 항목 선호도 조사 (Small)

n, m = map(int, input().split())
students = [input().split() for _ in range(n)]
queries = [input().split() for _ in range(m)]
answers = [0] * m

for i, q in enumerate(queries):
    for s in students:
        if q[0] not in [s[0],'-']: continue
        if q[1] not in [s[1],'-']: continue
        if q[2] not in [s[2],'-']: continue
        answers[i] += 1

print(*answers)
