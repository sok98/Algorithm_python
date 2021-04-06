import sys
input = sys.stdin.readline

N = int(input())
houses = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [list(False for _ in range(N)) for _ in range(N)]
blocks = {}


def DFS(i, j, number):
    stack = [[i, j]]
    blocks[number] = 0
    while stack:
        n = stack.pop()
        if houses[n[0]][n[1]] == 1 and visited[n[0]][n[1]] == False:
            visited[n[0]][n[1]] = True
            blocks[number] += 1

            if n[0] - 1 >= 0:
                stack.append([n[0] - 1, n[1]])
            if n[0] + 1 < N:
                stack.append([n[0] + 1, n[1]])
            if n[1] - 1 >= 0:
                stack.append([n[0], n[1] - 1])
            if n[1] + 1 < N:
                stack.append([n[0], n[1] + 1])


n = 0
for i in range(N):
    for j in range(N):
        if houses[i][j] == 1 and visited[i][j] == False:
            DFS(i, j, n)
            n += 1

print(len(blocks))
blocks = sorted(blocks.items(), key=lambda x: x[1])
for i in blocks:
    print(i[1])
