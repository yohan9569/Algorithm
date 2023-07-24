# 구현 / 브론즈 2 / 문자열 반복

T = int(input())
for t in range(T):
    R, S = input().split()
    print(''.join([i*int(R) for i in S]))
