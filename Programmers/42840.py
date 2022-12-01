# 완전탐색 lv1. 모의고사


def solution(answers):
    # 답안지 만들기
    a = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    b = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 1)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    
    # 맞춘 개수
    scores = [-1]
    for i in [a, b, c]:
        score = 0
        for x, y in zip(i, answers):
            if x == y:
                score += 1
        scores.append(score)
    
    # 최고점자 찾기
    return [j for j, v in enumerate(scores) if v==max(scores)]
