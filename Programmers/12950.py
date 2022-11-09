# 연습문제 lv1. 행렬의 덧셈

def solution(arr1, arr2):
    ans = []
    
    for i,j in zip(arr1, arr2):
        tmp = []
        
        for z in zip(i,j):
            tmp.append(sum(z))
            
        ans.append(tmp)
        
    return ans

  

    # better case
    return [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
