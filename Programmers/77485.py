# 2021 Dev-Matching  lv2. 행렬 테두리 회전하기


def rotate(matrix, sx, sy, ex, ey):
    tmp = [matrix[sx+1][sy]]
    
    for y in range(sy, ey+1):
        tmp.append(matrix[sx][y])
        matrix[sx][y] = tmp[-2]
        
    for x in range(sx+1, ex+1):
        tmp.append(matrix[x][ey])
        matrix[x][ey] = tmp[-2]
    
    for y in range(ey-1, sy-1, -1):
        tmp.append(matrix[ex][y])
        matrix[ex][y] = tmp[-2]
    
    for x in range(ex-1, sx, -1):
        tmp.append(matrix[x][sy])
        matrix[x][sy] = tmp[-2]
    
    return matrix, min(tmp)


def solution(rows, columns, queries):
    matrix = [[j +1 + columns*i for j in range(columns)] for i in range(rows)]
    answer = []
    
    for sx, sy, ex, ey in queries:
        matrix, ans = rotate(matrix, sx-1, sy-1, ex-1, ey-1)
        answer.append(ans)
    
    return answer
