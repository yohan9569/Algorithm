# 브루트포스 / 실버 4 / 한수


N = int(input())
n_han = 0

for n in range(1,N+1):
    if n < 100:
        n_han += 1
    else:
        a = [int(i) for i in list(str(n))]
        if a[0]-a[1] == a[1]-a[2]:
            n_han += 1
        else: pass

print(n_han)
