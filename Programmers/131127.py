# 연습문제 lv2. 할인 행사


from collections import Counter
def solution(want, number, discount):
    needs = {want[i] : number[i] for i in range(len(want))}
    ans = 0
    for i in range(len(discount)-9):
        ans += (needs == Counter(discount[i:i+10]))
    return ans
