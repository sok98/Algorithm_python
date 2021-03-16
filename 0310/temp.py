N, M = map(int, input().split())
tree = list(map(int, input().split()))
max_tree = max(tree)


def get_tree(height):
    total = 0
    for t in tree:
        if t > height:
            total += t-height
    return total


def find_height():
    # 구하고자 하는 나무의 합이 제일 높은 나무의 길이보다 크다면
    if M > tree[-1]:
        left = 0
    # 구하고자 하는 나무의 합이 제일 높은 나무의 길이보다 작다면
    else:
        left = max_tree - M

    right = max_tree - 1

    # 원하는 나무의 길이만큼을 최소한으로 자를 수 있는 절단기의 높이
    cut_height = 0

    while left <= right:
        pivot = (left+right)//2
        total = get_tree(pivot)
        if total == M:
            cut_height = pivot
            break
        elif total > M:
            cut_height = pivot
            left = pivot + 1
        else:
            right = pivot - 1

    return cut_height


print(find_height())
