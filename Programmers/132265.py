# 연습문제 lv2. 롤케이크 자르기


from collections import Counter
def solution(topping):
    front = set(topping)
    end = set()
    cnt = Counter(topping)
    ans = 0
    for i in range(len(topping)):
        t = topping.pop()
        cnt[t] -= 1
        if cnt[t] == 0:
            front.remove(t)
        end.add(t)
        if len(end) == len(front):
            ans += 1
    return ans
