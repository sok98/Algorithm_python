import sys
from itertools import combinations

N = int(sys.stdin.readline())
S = []
for i in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))

all_players = [i for i in range(N)]
teams = []
for t in combinations(all_players, N // 2):
    teams.append(list(t))

answer = []
for t in range(len(teams) // 2):

    A_stats = 0
    for i in teams[t]:
        for j in teams[t]:
            A_stats += S[i][j]

    B_stats = 0
    for i in teams[-(t + 1)]:
        for j in teams[-(t + 1)]:
            B_stats += S[i][j]

    answer.append(abs(A_stats - B_stats))

print(min(answer))
