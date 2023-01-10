# 1차원 배열 / 브론즈 5 / 과제 안 내신 분..?


ans = [*range(1, 31)]
while True:
    try:
        ans.remove(int(input()))
    except:
        break
for i in ans:
    print(i)
    
    
# another way
print(*sorted({*range(1,31)}-{*map(int,open(0))}))
