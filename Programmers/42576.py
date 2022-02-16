# 프로그래머스 # 해시 # 완주하지 못한 선수

def solution(participant, completion):
    
    from collections import Counter
    
    completion_map = Counter(completion)
    
    for user in participant:
      
        if user in completion_map:
            completion_map[user] -= 1
            
            if completion_map[user] <0:
                return user
              
        else: return user
