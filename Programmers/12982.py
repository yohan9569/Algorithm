# programmers 12982번 Summer/Winter Coding(~2018) lv.1 예산
# 괜히 while budget > 0 and answer < len(d) 이렇게 했다가 꼬였었다.


def solution(d, budget):
    d.sort()
    answer = 0
    
    for e in d:
        budget -= e
        
        if budget < 0:
            break
    
        answer += 1    
    
    return answer
