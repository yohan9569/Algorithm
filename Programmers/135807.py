# 연습문제 lv2. 숫자 카드 나누기
# 한 어레이의 공약수들 뽑고, 다른 어레이 나눌 수 있는지 체크
# 공약수 뽑기: 가장 작은 수들의 공약수의 약수들

def mkdivisors(n):
    divisors = set()
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors, reverse=True)

def get_a(array1, array2):
    a = []
    small = min(array1)
    divisors = mkdivisors(small)

    for d in divisors:
        flag = False
        for x in array1:
            if x%d != 0:
                flag = True
                break
        if flag:
            continue

        flag = False
        for y in array2:
            if y%d == 0:
                flag = True
                break
        if flag:
            continue

        a.append(d)
    return a

def solution(arrayA, arrayB):
    ans = [0]
    ans += get_a(arrayA, arrayB)
    ans += get_a(arrayB, arrayA)
    return max(ans)



# better way - functools.reduce 배웠다.
from math import gcd
from functools import reduce

def check(arrayA, arrayB):
    gcd_A = reduce(gcd, arrayA, arrayA[0])
    factors = [i for i in range(1, gcd_A//2+1) if not gcd_A % i]
    factors.append(gcd_A)
    for factor in factors[::-1]:
        if all(i % factor for i in arrayB):
            return gcd_A
    return 0

def solution(arrayA, arrayB):
    return max(check(arrayA, arrayB), check(arrayB, arrayA))
