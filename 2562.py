# 2562번 최댓값과 나온 순서
print(*max((v,i+1) for i,v in enumerate([int(input()) for _ in range(9)])), sep='\n')
