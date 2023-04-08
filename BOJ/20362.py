# 구현 / 브론즈 1 / 유니대전 퀴즈쇼


from collections import defaultdict

n,s = input().split()
d = defaultdict(int)
ans = 0

for _ in range(int(n)):
    x,y = input().split()
    if x == s:
        break
    d[y] += 1

print(d[y])



# another way - defaultdict 없이도 가능하다.
d[y] = d.get(y,0) + 1
