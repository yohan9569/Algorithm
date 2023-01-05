# 연습문제 lv2. 하노이의 탑


def hanoi(n, From, To, Side, ans):
    if n == 1:
        return ans + [[From, To]]
    # n-1을 옆으로 옮긴다.
    ans = hanoi(n-1, From, Side, To, ans)
    # 맨 밑장을 To로 옮긴다.
    ans.append([From, To])
    # n-1을 From으로 옮긴다.
    ans = hanoi(n-1, Side, To, From, ans)
    return ans


def solution(n):
    ans = hanoi(n, 1, 3, 2, [])
    return ans

  


# another way - yield 와 yield from 을 배웠다!
def solution(n):

    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    return ans
