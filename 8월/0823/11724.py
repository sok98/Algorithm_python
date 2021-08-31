import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {n:[] for n in range(1, N+1)}

for _ in range(M):
    u, v = map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)

visited = []
def dfs(n):
    stack = [n]
    while stack:
        num = stack.pop()
        if num not in visited:
            visited.append(num)
            stack.extend(dic[num])
    return 1

answer = 0
for i in range(1, N+1):
    if len(visited) == N:
        break
    if i not in visited:
        answer += dfs(i)

print(answer)