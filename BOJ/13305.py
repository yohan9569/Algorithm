# 그리디 / 실버 3 / 주유소


n = int(input())
dis = [*map(int, input().split())]
price = [*map(int,input().split())]

ans = 0
greed = price[0]

for i,v in enumerate(dis):
    ans += (v*greed)
    next = price[i+1]
    
    if greed>next: 
        greed = next

print(ans)
