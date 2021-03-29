import sys
N = int(sys.stdin.readline())

color = []
for i in range(N):
    color.append(list(map(int, sys.stdin.readline())))

d_rgb = {0: "R", 1: "G", 2: "B"}
d_choice = {"R": color[N - 1][0], "G": color[N - 1][1], "B": color[N - 1][2]}


def choice(string, i, j):
    string_add = string + d_rgb[j]
    if d_choice[string] in d_choice:
        return d_choice[string]
    else:
        d_choice[string] = choice(string)


print(min(choice("", N-1, 0), choice("", N-1, 1), choice("", N-1, 2)))
