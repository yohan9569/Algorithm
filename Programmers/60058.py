# 2020 KAKAO BLIND RECRUITMENT. lv2. 괄호 변환


def check(p):
    ans = 0
    for s in p:
        if s == '(':
            ans += 1
        else:
            ans -= 1
        if ans < 0:
            return False
    if ans == 0:
        return True

def solution(p):
    # 1.
    if not p or check(p):
        return p
    
    # 2.
    u = ''
    for s in p:
        u += s
        if u.count('(') == u.count(')'):
            break
    v = p[len(u):]
    
    # 3.
    if check(u):
        print(3)
        return u + solution(v)
    # 4.
    ans = '(' + solution(v) + ')' 
    ans2 = ''.join(')' if s=='(' else '(' for s in u[1:-1])
    return ans + ans2
