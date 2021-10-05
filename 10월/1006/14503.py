import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # 북 동 남 서
area = [list(map(int, input().split())) for _ in range(N)]

left_d = {0:3, 1:0, 2:1, 3:2}
xy_d = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

area[r][c] = -1 # 1
cnt = 1

while True:
    _d = d
    for _ in range(4):  # 2-a, b
        change = False
        _d = left_d[_d]
        dx = r+xy_d[_d][0]
        dy = c+xy_d[_d][1]
        if 0<= dx < N and 0<= dy < M and area[dx][dy] == 0:
            area[dx][dy] = -1
            cnt += 1
            d = _d
            r = dx
            c = dy
            change = True
            break

    if not change:  # 2-c, d
        _d = left_d[left_d[d]]  # 뒤쪽 방향
        r = r+xy_d[_d][0]
        c = c+xy_d[_d][1]
        if area[r][c] == 1: # 2-d
            break

print(cnt)