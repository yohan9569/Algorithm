# 월간 코드 챌린지 시즌2. lv2. 괄호 회전하기


def solution(s):
    ans = 0
    lens = len(s)
    brackets = ['()', '[]', '{}']
    
    if lens%2: return 0
    
    for i in range(lens):
        tmp = s[i:] + s[:i]
        
        if tmp[0] in [')', ']', '}'] or tmp[-1] in ['(', '[', '{']:
            continue
        
        for _ in range(lens//2):
            for b in brackets:
                tmp = tmp.replace(b, '')
            if not len(tmp):
                ans += 1
                break
    
    return ans
