# 스택/큐 lv2. 올바른 괄호

def solution(s):
    ans = 0    
    for i in s:
        if i == '(':
            ans += 1
        else:
            ans -= 1
        if ans == -1:
            return False
    
    if ans > 0:
        return False
    
    return True
