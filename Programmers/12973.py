# 2017 팁스타운 lv2. 짝지어 제거하기

def solution(s):
    
    stack = [1, s[0]] # 1 is for avoid index error
    for x in s[1:]:
        if stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
    
    return 1 if len(stack) == 1 else 0
