import sys
from itertools import combinations
N = int(sys.stdin.readline())

S = []
for i in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(i+1, N):
        S[i][j] += S[j][i]
        S[j][i] = 0

for team in combinations(range(N), N // 2):
    print(team[0], team[1])
    for i in combinations(team, 2):
        # S[i[0]][i[1]]
        print("짝", i)
