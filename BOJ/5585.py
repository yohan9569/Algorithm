# 그리디 / 브론즈 2 / 거스름돈


change = 1000 - int(input())
coins = [500,100,50,10,5,1]
ans = 0

for c in coins:
    n, change = divmod(change,c)
    ans += n
    if change==0:
        break

print(ans)


# another way - % 나머지 활용하는 참신한 발상

a=1000-int(input())
print(a//500 + a//100%5 + a//50%2 + a//10%5 + a//5%2 + a%5)
