# 월간 코드 챌린지 시즌3. lv2. n^2 배열 자르기


def solution(n, left, right):
    # 몫 = 2차원에서의 행, 나머지 = 2차원에서의 열
    return [max(i//n, i%n) + 1 for i in range(left, right+1)]




    ### previous version 1 - 시간 초과
    # 1
    arr2 = [[0] * n for _ in range(n)]
    
    # 2
    for i in range(n):
        tmp = i+1
        for j in range(tmp):
            arr2[i][j] = tmp
            arr2[j][i] = tmp
            
    # 3
    arr1 = []
    for arr in arr2:
        arr1 += arr
    
    # 4
    return [arr1[i] for i in range(left, right+1)]


    ### previous version 2 - 시간 초과
    return [max(i,j)+1 for j in range(n) for i in range(n)][left:right+1]
