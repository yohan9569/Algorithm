# 연습문제 lv1. 시저 암호


def solution(s, n):
    ans = ""
    
    up = range(65, 91)
    low = range(97, 123)
    for i in s:
        if i == ' ':
            ans += i
            continue
        
        old_asc = ord(i)
        new_asc = old_asc + n
        if (old_asc in up and new_asc in up) or (old_asc in low and new_asc in low):
            ans += chr(new_asc)
        else:
            ans += chr(new_asc-26)
            
    return ans


# better case
def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer
