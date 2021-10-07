from itertools import combinations
from copy import deepcopy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]   # 0: 빈칸, 1: 벽, 2: 바이러스

answer = 0
dir = [(-1,0), (0, -1), (1,0), (0,1)]

empty, virus = set(), set()
for x in range(N):
    for y in range(M):
        if arr[x][y] == 0:
            empty.add((x, y))
        if arr[x][y] == 2:
            virus.add((x,y))

for space in combinations(empty, 3):
    _arr = deepcopy(arr)
    for i, j in space:
        _arr[i][j] = 1

    _virus = deepcopy(virus)
    while _virus:
        x, y = _virus.pop()
        for d in dir:
            _x, _y = x+d[0], y+d[1]
            if 0 <= _x < N and 0 <= _y < M and _arr[_x][_y] == 0:
                _virus.add((_x, _y))
                _arr[_x][_y] = 2    

    cnt = 0
    for x in range(N):
        for y in range(M):
            if _arr[x][y] == 0:
                cnt += 1

    answer = max(answer, cnt)

print(answer)