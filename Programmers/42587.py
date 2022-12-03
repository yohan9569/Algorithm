# 스택/큐 lv2. 프린터


from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    cnt = 0
    
    while 1:
        m = max(q)
        
        # 1
        j = q.popleft()
        # 2
        if j < m:
            q.append(j)
        # 3
        else:
            cnt += 1
            if not location:
                return cnt
        
        # reposition
        location -= 1
        if location < 0:
            location = len(q)-1
