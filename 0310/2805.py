import math

N, M = map(int, input().split())    # N = 나무 개수 / M = 필요한 나무 길이
tree = list(map(int, input().split()))

min = 1000000000
max = 0
sum = 0
for i in tree:
    sum += i  # 모든 나무의 길이 구하기
    if i < min:  # 가장 작은 나무의 길이 구하기
        min = i
    if i > max:  # 가장 큰 나무의 길이 구하기
        max = i
temp = (sum - (min * N))  # pivot을 min으로 했을 때 가져갈 나무 길이

cut_tree = 0


def binary(p):
    global cut_tree
    global pivot
    cut_tree = 0
    get = 0
    for t in tree:
        if p < t:
            get += (t - p)
            cut_tree += 1

    if get < M:  # 이진탐색 결과가 필요한 나무보다 적을 때
        pivot = (max + p) // 2  # pivot 크게 다시 설정
        binary(pivot)
    elif get > M + cut_tree:  # 이진탐색 결과가 필요한 나무보다 확연히 많을 때
        pivot = (p + min) // 2  # pivot 작게 다시 설정
        binary(pivot)


if temp < M:  # 가져갈 나무가 필요한 나무보다 적을 때
    print(min - math.ceil(-temp / N))
elif temp == M:  # 가져갈 나무가 필요한 나무와 같을 때
    print(min)
else:  # 가져갈 나무가 필요한 나무보다 많을 때
    pivot = (max + min) // 2
    binary(pivot)  # 이진탐색
    print(pivot)
