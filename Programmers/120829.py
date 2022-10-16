# 코딩테스트 입문 lv1. 각도기

def solution(angle):
    if angle < 90:
        ans = 1
    elif angle == 90:
        ans = 2
    elif angle == 180:
        ans = 4
    else: 
        ans = 3
        
    return ans
