# 브루트포스 / 실버 5 / 셀프 넘버


origin = [i for i in range(1, 10001)]
n = 1
while n <= 10000:
    a = [int(i) for i in list(str(n))]

    notself = n + sum(a)
    if notself in origin:
        origin.remove(notself)

    # 다음 숫자로
    n += 1

for o in origin:
    print(o)




# 우수 풀이
self_number_set = {
    sum(map(lambda x: int(x), list(str(number)))) + number
    for number in range(1, 10000)
}

for i in range(1, 10000):
    if i not in self_number_set:
        print(i)
