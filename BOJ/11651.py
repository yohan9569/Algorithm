# 정렬 / 실버 5 / 좌표 정렬하기 2

from operator import itemgetter

xylist= [[*map(int, xy.split())] for xy in [*open(0)][1:]]

for x,y in sorted(xylist, key=itemgetter(1,0)): 
    print(x,y)
