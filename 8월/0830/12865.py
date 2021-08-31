import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [0]*(K+1)
items = [list(map(int, input().split())) for _ in range(N)] #[무게, 가치]

for i in range(N):
    for j in range(K, 0, -1):
        if items[i][0] <= j:
            bag[j] = max(bag[j], bag[j-items[i][0]] + items[i][1])

print(bag[-1])