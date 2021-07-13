import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(1, N+1)}
for i in range(M):
    k, v = map(int, sys.stdin.readline().split())
    graph[k].append(v)
    graph[v].append(k)

for k in graph:
    graph[k].sort()


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(sorted(graph[n], reverse=True))
    return visited


def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])
    return visited


print(' '.join(list(map(str, DFS(graph, V)))))
print(' '.join(list(map(str, BFS(graph, V)))))
