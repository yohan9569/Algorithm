# 연습문제 lv1. 문자열을 정수로 바꾸기

def solution(s):
    try:
        return int(s)
    except:
        if s[0] == '-':
            return -int(s[1:])
        else:
            return int(s[1:])

          
# int() recognizes and handles + -.
def solution(s):
    return int(s)
