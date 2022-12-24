# 월간 코드 챌린지 시즌2. lv2. 2개 이하로 다른 비트
# 풀이 아이디어: 이진수에서, 가장 낮은 자리에 있는 0을 1로 만들고, 다음 자리는 0으로 만든다.


def solution(numbers):    
    ans = []
    
    for n in numbers:
        b = bin(n)[2:]

        for i in range(len(b)-1, -1, -1):
            if b[i] == '0':
                if i == len(b)-1:
                    a = b[:-1] + '1'
                else:
                    a = b[:i] + '10' + b[i+2:]
                break
                
            if not i:
                a = '10' + b[1:]
        
        ans.append(int(a,2))
    
    return ans


# better case. 비트연산자 배웠다.
def solution(numbers):
    answer = []
    for val in numbers:
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer
