# 수학 / 실버 2 / 골든바흐의 추측


prime = set(range(2,10001))

for i in range(2,101):
    if i in prime:
        prime -= set(range(2*i,10001,i))

prime=sorted(list(prime))

# for a in [*map(int,[*open(0)][1:])]:
for a in [3,8,10,16]:
    for j in range(a//2,1,-1): # prime element로 돌리느라 고생
        if j in prime and a-j in prime:
            print(j,a-j)
            break
