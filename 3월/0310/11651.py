N = int(input())
dots = []
for i in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(dots[i][0], dots[i][1])
