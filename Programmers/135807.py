# 연습문제 lv2. 숫자 카드 나누기


# 한 어레이의 공약수들 뽑고, 다른 어레이 나눌 수 있는지 체크
# 공약수 뽑기: 가장 작은 수의 약수들 or 가장 작은 수들의 공약수의 약수들?

from math import gcd
def solution(arrayA, arrayB):
    ans = [0]
    
    # arrayA
    arrayA.sort()
    a,b = arrayA[:2]
    gcd(a,b)
