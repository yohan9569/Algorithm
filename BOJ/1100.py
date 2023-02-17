# 문자열 / 브론즈 2 / 하얀 칸

cnt = 0
for i in range(8):
    for j in input()[i%2::2]:
        if j=='F':
            cnt+=1
print(cnt)
