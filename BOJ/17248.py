# 수학 / 브론즈 2 / 물리 공부


for _ in range(int(input())):
    x,y,z = map(int, input().split())
    z2,c = z,0
    
    while x<y:
        x+=z
        z+=z2
        c+=1
    
    print(c)
