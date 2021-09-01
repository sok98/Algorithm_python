import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = int(1e9)
point = [INF]*(V+1)
graph = {n:[] for n in range(1, V+1)}    # 시작 노드 : [(도착 노드, 가중치)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(n):
    queue = []
    heapq.heappush(queue, (0, n))
    point[n] = 0

    while queue:
        start, end = heapq.heappop(queue)
        if point[end] < start:
            continue

        for node in graph[end]:
            cost = start + node[1]

            if cost < point[node[0]]:
                point[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))

dijkstra(K)
for p in point[1:]:
    if p == INF:
        print("INF")
    else:
        print(p)


