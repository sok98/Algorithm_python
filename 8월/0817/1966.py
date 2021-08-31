import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    cnt = 0
    target = queue[M]
    queue[M] = -1   # 다른 값들과 구분

    while max(queue) > target:
        cnt += 1
        pop = queue.index(max(queue))
        queue = queue[pop+1:] + queue[:pop]
    print(cnt + queue[:queue.index(-1)].count(target) + 1)