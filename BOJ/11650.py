# boj 백준 정렬 11650번 좌표 정렬하기

from operator import itemgetter

xylist= [[*map(int, xy.split())] for xy in [*open(0)][1:]]

for x,y in sorted(xylist, key=itemgetter(0,1)):
    print(x,y)

    
# 그냥 sorted하면 알아서 그렇게 해준다.
# for i in sorted(xylist): print(*i)
