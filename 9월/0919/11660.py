import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# board의 가로 세로 첫 줄은 0으로 초기화. board의 길이는 N+1이 되고 값은 (1,1)부터 있다.
board = [[0 for _ in range(N+1)]]
for _ in range(N):
    board.append([0])
    board[-1].extend(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        board[i][j] += board[i-1][j] + board[i][j-1] - board[i-1][j-1]
        
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(board[x2][y2] - board[x1-1][y2] - board[x2][y1-1] + board[x1-1][y1-1])