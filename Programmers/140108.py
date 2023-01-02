# 연습문제 lv1. 문자열 나누기


def solution(s):
    answer = 0
    while s:
        cnt_x = 0
        cnt_ect = 0
        for i, v in enumerate(s):
            if v == s[0]:
                cnt_x += 1
            else:
                cnt_ect += 1
                
            if cnt_x == cnt_ect:
                answer += 1
                s = s[i+1:]
                break
            elif i == len(s)-1:
                answer += 1
                s = ''
    return answer
  
  
  # better way
  def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer
