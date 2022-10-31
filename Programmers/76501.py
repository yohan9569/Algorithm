# 월간 코드 챌린지 시즌2 lv1. 음양 더하기

def solution(absolutes, signs):
    ans = 0
    
    for i,v in enumerate(signs):
        if v:
            ans+=absolutes[i]
        else:
            ans-=absolutes[i]
    
    return ans
