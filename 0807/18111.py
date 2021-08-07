import sys
input = sys.stdin.readline
count, height = -1, 0

n, m, b = map(int, input().split())
land = []
for _ in range(n):
    land.extend(list(map(int, input().split())))
land.sort(reverse=True)

for h in range(land[-1], land[0]+1):    # h = 목표 높이
    c, tmp = 0, b
    for l in land:                      # l = 좌표의 높이
        if l > h:   # 블록 제거
            c += (l-h)*2
            tmp += l-h
        elif l < h: # 블록 쌓기
            c += h-l
            tmp -= h-l
    
    if tmp < 0:
        break

    if count == -1 or c <= count:
        count = c
        height = h


print(count, height)
