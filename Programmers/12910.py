# 연습문제 lv1. 나누어 떨어지는 숫자 배열

def solution(arr, div):
    ans = [i for i in arr if i%div==0]
    
    if len(ans)==0:
        return [-1]
    
    return sorted(ans)
