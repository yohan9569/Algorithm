# 프로그래머스 64061 lv1 크레인 인형뽑기 
# 문제가 헷갈렸다. 당연히 board가 세로로 주어진 줄


def solution(board, moves):
    bas = [-1]
    res = 0
    
    for m in moves:
        for b in range(len(board)):
            tmp = board[b][m-1]
            
            if tmp!=0:
                board[b][m-1] = 0
                
                if tmp == bas[-1]:
                    bas.pop()
                    res+=2
                    
                else:
                    bas.append(tmp)
                    
                break
                
    return res
