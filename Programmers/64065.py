# 2019 카카오 개발자 겨울 인턴십. lv2. 튜플


from collections import Counter

def solution(s):
    s = s.replace('{', '').replace('}', '')
    l = s.split(',')
    return [int(elem) for elem, _ in Counter(l).most_common()]
