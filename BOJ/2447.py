# 백준 2447번 재귀 - 별 찍기-10
# 방법: 전체가 *로 채워진 어레이에서 특정 부분을 공백으로 대체

def space(n,ri,ci):
    if n==3: arr[ri + 1][ci + 1] = " "
    else: 
        next = n//3
        for r in range(ri+next, ri+next*2):
            for c in range(ci+next, ci+next*2):
                arr[r][c]=" "

        for i in range(3):
            for j in range(3):
                if i==1 and j==1: continue
                space(next, ri+next*i, ci+next*j)
                
def print_star(n, arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end="")
        print()
        
        
n=int(input())
arr = [["*"]* n for _ in range(n)]
space(n,0,0)
print_star(n, arr)


"""
다 짜고 실패한 이유: 
arr=[["*"]*n]*n => 얕은 복사
"""
