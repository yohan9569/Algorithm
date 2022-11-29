# 스택/큐 lv2. 기능개발


def solution(progs, spds):
    ans = []
    
    # 모든 기능이 배포될 때까지 반복
    while progs:
        
        # 하루 진도 나가기
        for i, s in enumerate(spds):
            progs[i] += s
        
        # 앞쪽부터 확인 후 배포, 카운팅
        cnt = 0
        for p in progs:
            if p >= 100:
                progs = progs[1:]
                spds.pop(0)
                cnt += 1
            else:
                break
        
        # 배포가 됐다면, 배포된 기능의 수를 답지에 추가
        if cnt:
            ans.append(cnt)
    
    return ans
