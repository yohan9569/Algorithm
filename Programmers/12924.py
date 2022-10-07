# 연습문제 lv2. 숫자의 표현

def solution(n):
    ans = 0
    
    if n < 3:
        return 1
    
    for i in range(1, n//2+2):
        sum_ = 0
        plus = i
        
        while sum_ < n:
            sum_ += plus
            plus += 1
            
            if sum_ == n:
                ans += 1
                break
    
    return ans+1
