# JadenCase 문자열 만들기

def solution(s):
    words = [a.lower() for a in s.split()]
    
    # 스페이스의 위치 저장
    spaces = []
    for i, v in enumerate(s):
        if v==" ":
            spaces.append(i)
    
    # 스페이스 제외한 답
    ans = "".join([a[0].upper() + a[1:].lower() for a in words])
    
    # 답에 스페이스 추가
    for i in spaces:
        ans = ans[:i] + " " + ans[i:]
    
    return ans
