N, M = map(int, input().split())

def check(chess:list, a,b, change:list) ->int:
    bw=0
    wb=0
    for i,x in enumerate(chess[a:a+8]):
        for j,y in enumerate(x[b:b+8]):
            if (i%2==0 and j%2==0)or(i%2==1 and j%2==1) :
                if y=='W': bw+=1
                else: wb+=1
            else: 
                if y=='B': bw+=1
                else: wb+=1
    # return bw, wb
    change.append(bw)
    change.append(wb)

change=[]
chess=[]
for _ in range(N):
    chess.append(input())

for i in range(N-7):
    for j in range(M-7):
        check(chess,i,j, change)
print(min(change))