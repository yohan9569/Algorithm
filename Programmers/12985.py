# 2017 팁스타운 lv2. 예상 대진표

def solution(n,a,b):
    cnt = 1
    
    while abs(b-a) > 1 or max(a,b)%2 !=0 :
        if a%2 == 0:
            a = a//2
        else:
            a = (a//2)+1
        if b%2 == 0:
            b = b//2
        else:
            b = (b//2)+1
        cnt += 1
        
    return cnt


# better case
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
