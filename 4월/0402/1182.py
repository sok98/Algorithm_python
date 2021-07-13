import sys
import itertools

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(1, N + 1):
    for i in itertools.combinations(numbers, i):
        if sum(i) == S:
            answer += 1
print(answer)
