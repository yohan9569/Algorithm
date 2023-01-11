# 정렬 / 브론즈 2 / 대표값2


l = sorted(int(input()) for _ in range(5))
print(sum(l)//5)
print(l[2])


# short coding
print(sum(l:=sorted(map(int,open(0))))//5,l[2])
