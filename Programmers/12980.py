# Summer/Winter Coding(~2018) lv2. 점프와 순간 이동


def solution(n):
    ans = 0
    
    while n:
        if n%2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1
    
    return ans


    # better case
    return bin(n).count('1')
