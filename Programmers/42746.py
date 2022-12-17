# 정렬 lv2. 가장 큰 수


# https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html 참고함.
def solution(numbers):
    numbers = [*map(str, numbers)]
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
