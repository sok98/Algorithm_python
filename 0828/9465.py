import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stikers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(stikers[0][0], stikers[1][0]))

    else:
        stikers[0][1] += stikers[1][0]
        stikers[1][1] += stikers[0][0]
        for i in range(2, n):
            stikers[0][i] += max(stikers[1][i-1], stikers[1][i-2])
            stikers[1][i] += max(stikers[0][i-1], stikers[0][i-2])

        print(max(stikers[0][n-1], stikers[1][n-1]))
        