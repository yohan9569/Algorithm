# 연습문제 lv1. 숫자 짝꿍


from collections import Counter
def solution(X, Y):
    cx, cy = Counter(X), Counter(Y)
    shared = ''.join(k * min(cx[k], cy[k]) for k in cx if k in cy)
    ans = ''.join(sorted(shared, reverse=True))
    if not ans:
        return '-1'
    elif ans[0]=='0':
        return '0'
    return ans
