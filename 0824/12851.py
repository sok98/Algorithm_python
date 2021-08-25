import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if K == N:      # 둘이 같은 위치에 있을 때
    print(0)
    print(1)
elif K < N :    # 동생이 뒤에 있을 때
    print(N-K)
    print(1)

else:
    visited = [0 for _ in range(100001)]
    queue = [N]
    time = 0

    while queue:
        time += 1
        next_queue = []
        for n in queue:
            if (n >= 0 and n <= 100000) and (visited[n] == 0 or visited[n] == time):
                next_queue.extend([n*2, n-1, n+1])
                visited[n] = time

        if next_queue.count(K) > 0:
            print(time) 
            print(next_queue.count(K))
            break
        
        queue = next_queue