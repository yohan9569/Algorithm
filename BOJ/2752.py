# 정렬 / 브론즈 4 / 세수정렬

print(*sorted(map(int, input().split())))


# another way - key 활용
print(*sorted(input().split(),key=int))
