from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
people = deque(range(1, N+1))

answer = []
while people:
    people.rotate(-K)
    n = people.pop()
    answer.append(n)

# print(answer)
print("<", end='')
for i in answer[:-1]:
    print(i, end=", ")
print(answer[-1], end=">")
