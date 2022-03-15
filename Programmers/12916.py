# 12916 문자열 내 p와 y의 개수

def solution(s):
    s = s.lower()
    p = sum(1 if i=='p' else 0 for i in s)
    y = sum(1 if i=='y' else 0 for i in s)
    
    if p != y: 
      return False
    else: 
      return True
    
    
# 우수 풀이
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
