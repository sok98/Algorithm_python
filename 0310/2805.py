import math

N, M = map(int, input().split())    # N = 나무 개수 / M = 필요한 나무 길이
tree = list(map(int, input().split()))

min = min(tree)
max = max(tree)
sum = sum(tree)
tall = 0  # 톱 길이보다 큰 나무 개수 저장

get = (sum - (min * N))  # pivot을 min으로 했을 때 가져갈 나무 길이


def binary(p):
    g = 0
    global tall
    tall = 0
    for t in tree:
        if p < t:
            g += (t - p)
            tall += 1
    return g


if get < M:  # 가져갈 나무가 필요한 나무보다 적을 때
    print(min - math.ceil((M-get) / N))
elif get == M:  # 가져갈 나무가 필요한 나무와 같을 때
    print(min)

else:  # 가져갈 나무가 필요한 나무보다 많을 때
    cut = 0
    while max >= min:
        pivot = (max + min) // 2
        get = binary(pivot)  # 이진탐색

        if get < M:    # 이진탐색 결과가 필요한 나무보다 적을 때
            max = pivot - 1

        elif get > M+tall:  # 이진탐색 결과가 필요한 나무보다 많을 때
            cut = pivot
            min = pivot + 1

        else:
            cut = pivot
            break
    print(cut)
