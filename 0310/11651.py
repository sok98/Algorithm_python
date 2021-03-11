N = int(input())
dots = []
for i in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))

for i in dots:
    print(i)
