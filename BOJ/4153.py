# 수학 / 브론즈 3 / 직각삼각형


while True:
    s = list(map(int,input().split()))
    a,b,c = sorted(s)
    
    if c == 0:
      break
    elif c**2 == a**2+b**2:
      print('right')
    else:
      print('wrong')
