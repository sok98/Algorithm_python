import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

answer = 0
tmp = [(0, 1), (0, -1), (1, 0), (-1, 0)]

stack = set([(0, 0, board[0][0])])  # set으로 안하면 시간초과
while stack:
    x, y, v = stack.pop()
    answer = max(answer, len(v))

    for _x, _y in tmp:
        a = x+_x
        b = y+_y
        if 0 <= a < R and 0 <= b < C and board[a][b] not in v:
            stack.add((a, b, v+board[a][b]))

print(answer)


# def move(x, y, v):
#     global answer
#     answer = max(answer, len(v))

#     for _x, _y in tmp:
#         a = x+_x
#         b = y+_y
#         if 0 <= a < R and 0 <= b < C and board[a][b] not in v:
#             move(a, b, v+board[a][b])            

# move(0, 0, board[0][0])
# print(answer)