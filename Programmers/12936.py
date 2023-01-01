# 연습문제 lv2. 줄 서는 방법


from math import factorial
def solution(n, k):
    people = [*range(1, n+1)]
    ans = []
    k -= 1 # important
    for i in range(n, 0, -1):
        q, k = divmod(k, factorial(i-1))
        ans.append(people.pop(q))
    return ans
