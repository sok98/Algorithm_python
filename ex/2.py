N = int(input())
point = list(map(int, list(input())))
k = 0
p = []


def check(n):
    global k
    if n == N - 1:
        k += 1
    else:
        if n+1 <= N-1 and point[n + 1] != 0:
            check(n + 1)
        if n+2 <= N-1 and point[n + 2] != 0:
            check(n + 2)


check(0)
print(k)
