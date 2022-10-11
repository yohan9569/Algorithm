# 완전탐색 lv2. 카펫

def solution(brown, yellow):
    divisors = []
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            divisors.append(i)
    
    for l in divisors:
        width, length = (yellow/l + 2), (l+2)
        if brown + yellow == width * length:
            return [width, length]
