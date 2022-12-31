# 연습문제 lv1. 옹알이 (2)


def solution(babbling):
    able = ["aya", "ye", "woo", "ma"]
    unable = [a*2 for a in able]
    ans = 0
    for s in babbling:
        flag = False
        # 연속 같은 발음 여부
        for u in unable:
            if u in s:
                flag = True
                break
        if flag:
            continue
        # 가능한 발음 외에 스펠링 여부
        for a in able:
            s = s.replace(a, '-')
        s = s.replace('-', '')
        if s:
            continue
        ans += 1
    return ans


# better way
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
