import sys
inpput = sys.stdin.readline

N = int(input())
computer = {n:set([]) for n in range(1,N+1)}

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    computer[x].add(y)
    computer[y].add(x)

answer = []
stack = [1]
while stack:
    n = stack.pop()
    if n not in answer:
        answer.append(n)
        stack.extend(computer[n])

print(len(answer)-1)    # 1번 컴퓨터 빼기