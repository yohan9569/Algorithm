# boj 백준 정렬 18870번 좌표 압축 # 자기보다 작은 수의 숫자 구하기

x = [*map(int, [*open(0)][1].split())]
xs = sorted(set(x))
xd = {xs[i]:i for i in range(len(xs))} # dict가 핵심

ans = [xd[j] for j in x]

print(*ans)
