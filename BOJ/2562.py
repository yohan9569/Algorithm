# 구현 / 브론즈 3 / 최댓값

print(*max((v,i+1) for i,v in enumerate([int(input()) for _ in range(9)])), sep='\n')
