T = int(input())
for t in range(T):
    R, S = input().split()
    print(''.join([i*int(R) for i in S]))
