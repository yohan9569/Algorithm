# 수학 / 브론즈 2 / 벌집
# 거쳐야 하는 방 수를 기준으로 그룹화 시키면 규칙이 나옴.

n = int(input())
cnt = 1

while n>1:
    n -= (6*cnt)
    cnt += 1
    
print(cnt)
