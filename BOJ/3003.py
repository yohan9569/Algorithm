# 입출력과 사칙연산 / 브론즈5 / 킹, 퀸, 룩, 비숍, 나이트, 폰

Input = [*map(int, input().split())]
correct = [1, 1, 2, 2, 2, 8]
print(' '.join(str(correct[i]-Input[i]) for i in range(len(Input))))
