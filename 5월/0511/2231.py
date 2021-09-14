import sys
input = sys.stdin.readline

N = int(input())

answer = N // 2

while N > answer:
    sum = answer
    for i in str(answer):
        sum += int(i)
    if sum == N:
        break
    answer += 1

if answer >= N:
    answer = 0

print(answer)
