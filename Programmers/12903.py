# 연습문제 lv1. 가운데 글자 가져오기

def solution(s):
    q,r = divmod(len(s),2)
    
    if r:
        return s[q]
    else:
        return s[q-1:q+1]
