n, m = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(m)]
case = []


def search(y, x, move):
    move += temp[y][x]
    if x == n - 1 and y == m - 1:
        case.append(move)
    else:
        if y != m - 1:
            search(y + 1, x, move)
        if x != n - 1:
            search(y, x + 1, move)


search(0, 0, 0)
print(max(case))
