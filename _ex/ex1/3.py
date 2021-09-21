N = int(input())
temp = [list(map(int, input())) for _ in range(N)]
size = [0 for _ in range(N)]

for i in range(N):
    for j in range(N):
        if temp[i][j] == 1 and temp[j][i] == 1:


for n in range(size):
    print('size[{0}]:{1}', n+1, size[n])
