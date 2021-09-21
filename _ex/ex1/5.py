n, m = map(int, input().split())
temp = [list(input()) for _ in range(m)]
case = []
before_x = 100


def search(y, x, move):
    global before_x

    if y == m - 1:
        case.append(move)
    elif temp[y + 1][x] == '.':
        before_x = 100
        search(y + 1, x, move)
    else:
        if x != n - 1 and x+1 != before_x and temp[y][x + 1] == '.':
            before_x = x
            move += 1
            search(y, x+1, move)
        if x != 0 and x-1 != before_x and temp[y][x - 1] == '.':
            before_x = x
            move += 1
            search(y, x - 1, move)


for i in range(n):
    if temp[0][i] == 'c':
        k = 0
        search(0, i, k)

if not case:
    print(-1)
else:
    print(min(case))
