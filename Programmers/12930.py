# 연습문제 lv1. 이상한 문자 만들기

def solution(s):
    cnt = 0
    ans = ''
    for v in s:
        if v==' ':
            cnt=0
            ans+=v
            continue
        elif cnt%2==0:
            ans+=v.upper()
        else:
            ans+=v.lower()
        cnt+=1
    return ans
