# 스택/큐 lv2. 주식가격

# 슬라이싱으로 for문을 돌리는 부분에서 효율성이 계속 걸렸다. 복사본으로 리스트를 만드는 과정이 추가되는 것 같다.
# len() == O(1) # max() & min() == O(n) # slice == O(k) # https://wiki.python.org/moin/TimeComplexity
# enumerate > range(len()) # https://stackoverflow.com/questions/24150762


def solution(prices):
    ans = []
    
    for i, p in enumerate(prices):
        t = 0
        # for p2 in prices[i+1:]:
        for j in range(i+1, len(prices)):
            t += 1
            if p > prices[j]:
                break
        ans.append(t)

    return ans
