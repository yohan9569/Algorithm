# boj 백준 10871 X보다 작은 수

x=int(input().split()[1])
print(' '.join(i for i in input().split() if int(i)<x))
