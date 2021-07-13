import sys
input = sys.stdin.readline

n = int(input())
score = []

for _ in range(n):
    score.append(int(input()))

if n <= 2:
    print(sum(score))
else:
    total_score = [[score[i], score[i]] for i in range(n)]
    # 0 -> 1 이동
    total_score[1][0] += score[0]

    for i in range(2, n):
        total_score[i][0] += total_score[i - 1][1]
        total_score[i][1] += max(total_score[i-2])

    print(max(total_score[n-1]))
