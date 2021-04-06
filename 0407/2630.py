import sys
input = sys.stdin.readline

N = int(input())
colors = []
for n in range(N):
    colors.append(list(map(int, input().split())))

print(colors)

white = 0
blue = 0


def check(start_i, start_j, n):
    global white, blue
    std = colors[start_i][start_j]
    for i in range(start_i, start_i + n):
        for j in range(start_j, start_j + n):
            if std != colors[i][j]:
                check(start_i, start_j, n//2)
                check(start_i, start_j + n//2, n//2)
                check(start_i + n//2, start_j, n//2)
                check(start_i + n//2, start_j + n//2, n//2)
                return
    if std == 0:
        white += 1
    else:
        blue += 1
    return


check(0, 0, N)
print(white)
print(blue)
