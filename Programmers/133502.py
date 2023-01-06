# 연습문제 lv1. 햄버거 만들기
# 처음에는 string으로 만들어 replace('1231', '', 1) 했으나 시간초과가 발생했다.


def solution(ingredient):
    stack = []
    ans = 0
    
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            ans += 1
            del stack[-4:]
                
    return ans
