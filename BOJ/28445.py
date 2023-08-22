# 구현 / 실버 5 / 알록달록 앵무새
# 처음에는 itertools.product 사용했지만, 굳이 필요 없었다.


colors = sorted(set(input().split()+input().split()))

for body in colors:
    for tail in colors:
        print(body, tail)
