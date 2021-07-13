import sys
N, K = map(int, sys.stdin.readline().split())
coin = []
answer = 0

for i in range(N):
    coin.append(int(sys.stdin.readline()))

for i in range(len(coin) - 1, -1, -1):
    if K == 0:
        break
    if K // coin[i] != 0:
        answer += K // coin[i]
        K = K % coin[i]

print(answer)
