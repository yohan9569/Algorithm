# 연습문제 lv2. 연속 부분 수열 합의 개수


def solution(elements):
    ans = set()
    ext = elements + elements[:-1]
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            ans.add(sum(ext[j:j+i]))
    return len(ans)
