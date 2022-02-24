# 프로그래머스 # 탐욕법 # 체육복
# 전체 리스트를 만들어서 비교하려고 해서 고생했음.

def solution(n, lost, reserve):
    lost_ = set(lost) - set(reserve)
    reserve_ = set(reserve) - set(lost)
    
    for i in lost_:
        if i-1 in reserve_:
            reserve_.remove(i-1)
            
        elif i+1 in reserve_:
            reserve_.remove(i+1)
            
        else: n -=1
          
    return n
