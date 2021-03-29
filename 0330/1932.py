import sys
n = int(sys.stdin.readline())
number = []
for i in range(n):
    number.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            number[i][0] += number[i - 1][0]
        elif j == i:
            number[i][j] += number[i-1][j-1]
        else:
            number[i][j] += max(number[i - 1][j - 1], number[i - 1][j])

answer = 0
for k in range(n):
    if answer < number[n - 1][k]:
        answer = number[n - 1][k]

print(answer)
