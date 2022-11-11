# 연습문제 lv1. 최대공약수와 최소공배수

def solution(n, m):
    from math import gcd
    return [gcd(n,m), (n*m // gcd(n,m))]
