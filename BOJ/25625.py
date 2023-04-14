# 수학 / 브론즈 4 / 샤틀버스

x,y=map(int,input().split())
print(x+y if x>y else y-x)


# another way - 음수%양수
print((y-x)%(2*x))
