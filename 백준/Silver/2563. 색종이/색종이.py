n = int(input())
papers = [map(int, input().split()) for _ in range(n)]
board = [[0]*100 for _ in range(100)]

for left, bottom in papers:
    for i in range(bottom, bottom+10):
        board[i][left:left+10] = [1]*10

print(sum(map(sum, board)))