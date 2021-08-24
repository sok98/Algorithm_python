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
    time = 1
    queue = [K-1, K+1]
    if K % 2 == 0:
        queue.append(K//2)
   
    while queue:
        tmp = []
        time += 1
        for k in queue:
            if k % 2 == 0:
                tmp.append(k//2)
            tmp.append(k-1)
            tmp.append(k+1)
        
        if tmp.count(N) > 0:
            print(time)
            print(tmp.count(N))
            break

        queue = list(set(tmp))