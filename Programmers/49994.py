# Summer/Winter Coding(~2018). lv2. 방문 길이


def move(prev, d):
    # now 구하기
    if d == 'U':
        now = (prev[0] + 1, prev[1])
    elif d== 'D':
        now = (prev[0] - 1, prev[1])
    elif d== 'R':
        now = (prev[0], prev[1] + 1)
    else:
        now = (prev[0], prev[1] - 1)
    
    # 좌표평면 벗어날 경우
    if not now[0] in range(-5, 6) or not now[1] in range(-5, 6):
        return None, prev
    
    road = frozenset({prev, now})
    return road, now


def solution(dirs):
    ans = set()
    point = (0,0)
    
    for d in dirs:
        road, point = move(point, d)
        ans.add(road)
    
    ans.discard(None)
    return len(ans)


  

# other case
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
