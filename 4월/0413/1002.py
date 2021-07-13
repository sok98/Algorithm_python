import sys
input = sys.stdin.readline

T = int(input())
point = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    # 두 점 사이의 거리
    n = ((point[i][3] - point[i][0]) ** 2 +
         (point[i][4] - point[i][1]) ** 2) ** 0.5
    # 각 점에서 적까지의 거리
    k1, k2 = point[i][2], point[i][5]

    # 두 원이 같을 때
    if n == 0 and k1 == k2:
        print(-1)
    # 두 원이 겹쳐 두 점에서 만날 때
    elif abs(k2 - k1) < n < k1 + k2:
        print(2)
    # 두 원이 내접하거나 외접할 때
    elif n == k1 + k2 or n == abs(k2 - k1):
        print(1)
    # 두 원이 만나지 않을 때
    else:
        print(0)
