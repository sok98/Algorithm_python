N, K = map(int, input().split())
numbers = list(map(int, input().split()))
if N//(K-1) == 0:
    print(N // (K - 1))
else:
    print(N // (K-1) + 1)
