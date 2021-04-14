from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = []
for i in combinations(cards, 3):
    if sum(i) <= M:
        answer.append(sum(i))

print(max(answer))
