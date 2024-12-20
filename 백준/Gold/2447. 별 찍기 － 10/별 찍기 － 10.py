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