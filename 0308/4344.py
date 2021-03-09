# 백준 4344번


c = int(input())
m = []

for i in range(c):
    k = 0
    n = list(map(int, input().split()))

    s = sum(n[1:])

    for j in n[1::]:  # 평균 이상 값 찾기
        if j > (s / n[0]):
            k += 1
    m += [k/n[0] * 100]

for i in m:
    print(f'{i:.3f}%')
