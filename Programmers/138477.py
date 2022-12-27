# 연습문제 lv1. 명예의 전당 (1)


def solution(k, score):
    answer = []
    fame = []
    
    for s in score:
        if len(fame) < k:
            fame.append(s)
        elif fame[-1] < s:
            fame[-1] = s
            
        fame.sort(reverse=True)
        answer.append(fame[-1])
        
    return answer
  
  
  # better case
  def solution(k, score):
    q = []
    answer = []
    
    for s in score:
        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer
