# 연습문제(dp) lv2. 땅따먹기


def solution(land):
    dp = [[0]*4 for i in range(len(land))]
    dp[0] = land[0]
    
    for i in range(1, len(dp)):
        for j in range(4):
            dp[i][j] = max(dp[i-1][k] for k in range(4) if k!=j) + land[i][j]

    return max(dp[-1])
