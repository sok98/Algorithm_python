import sys
N = int(sys.stdin.readline())

color = []
for i in range(N):
    color.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    color[i][0] += min(color[i - 1][1], color[i - 1][2])
    color[i][1] += min(color[i - 1][0], color[i - 1][2])
    color[i][2] += min(color[i - 1][0], color[i - 1][1])

answer = min(color[N - 1][0], color[N - 1][1], color[N - 1][2])
print(answer)
