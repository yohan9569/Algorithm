# 2019 KAKAO BLIND RECRUITMENT. lv1. 실패율


from collections import defaultdict

def solution(N, stages):
    dd = defaultdict(list)
    
    # 정답률 = key, 해당 스테이지 담긴 리스트 = value
    for i in range(1, N+1):
        tmp = [s for s in stages if s>=i]
        if len(tmp):
            dd[tmp.count(i) / len(tmp)].append(i) 
        else:
            dd[0].append(i)
    
    # 정답률 내림차순 정렬 후 value 하나의 리스트로 묶어주기
    ans = []
    for item in sorted(dd.items(), reverse=True):
        ans += item[1]
    
    return ans
