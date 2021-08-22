import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[0 for _ in range(M)] for _ in range(N)]
    land = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        land[y][x] = 1

    def dfs(x, y):
        stack = [(x, y)]
        while stack :
            x, y = stack.pop()
            try:
                if x >=0 and y >= 0 and visited[x][y] == 0 and land[x][y] == 1:
                    visited[x][y] = 1

                    stack.append((x-1, y))
                    stack.append((x+1, y))
                    stack.append((x, y-1))
                    stack.append((x, y+1))
            except IndexError:
                continue

        return 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and land[i][j] == 1:
                answer += dfs(i, j)
    
    print(answer)
