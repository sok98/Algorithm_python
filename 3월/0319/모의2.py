T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    if N // 5 == 0:
        print(0)
    elif N // 5 <= M // 7:
        print(N // 5)
    else:
        print(M//7 + ((N-(M//7)*5)+(M-(M//7)*7))//12)
