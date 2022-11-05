# 연습문제 lv1. 문자열 다루기 기본

def solution(s):
    try:
        int(s)
        if len(s) in [4,6]:
            return True
        return False
    except:
        return False
    
    
    # better case
    return s.isdigit() and len(s) in (4, 6)
