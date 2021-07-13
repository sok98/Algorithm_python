from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())


for i in combinations(range(1, N + 1), M):
    for j in range(M):
        print(i[j], end=" ")
    print()
