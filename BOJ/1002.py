# boj 백준 기본 수학 2 1002번 터렛

for a in ['0 0 13 40 0 37','0 0 3 0 7 4','1 1 1 1 1 5']:
    x1,y1,r1,x2,y2,r2 = map(int, a.split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    rmr = abs(r1-r2)
    rpr = r1+r2
    
    if d==0 and rmr==0: print(-1) # 이 순서가 아래 있어서 틀렸음
    elif rmr<d and d<rpr: print(2)
    elif rpr==d or rmr==d: print(1)
    elif rpr<d or d<rmr: print(0)
    else: print(0)
