import sys
input = sys.stdin.readline()

# N = int(input())
N = 6
step = [0]*(N+1)
count = [0]*(N+1)

count[0] = 0
sum = 0

for i in range(1, 3):  # 1, 2 계단은 무조건 밟음
    step[i] = int(input())
    step[i] += sum
    sum = step[i]
    count[i] += 1


for i in range(3, N+1):
    value = int(input())

    if count[i-1] >= 2 or (step[i-1] < step[i-2]):
        step[i] = step[i-2]+value
    else:
        step[i] = step[i-1]+value
        count[i] = count[i-1]+1

print(step[N])
