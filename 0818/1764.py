import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n = set()
for _ in range(N):
    n.add(input().rstrip())

m = set()
for _ in range(M):
    m.add(input().rstrip())

answer = sorted(n&m)
print(len(answer))
for i in answer:
    print(i)