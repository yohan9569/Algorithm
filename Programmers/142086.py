# 연습문제 lv1. 가장 가까운 같은 글자

def solution(string):
    dic = {s : -1 for s in string}
    ans = []
    for i, s in enumerate(string):
        tmp = dic[s]
        if tmp == -1:
            ans.append(tmp)
        else:
            ans.append(i-tmp)
        dic[s] = i
    return ans
