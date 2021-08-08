import sys
input = sys.stdin.readline

n = int(input())

numbers = [0, 1]
for i in range(2, n+1):
    numbers.append(numbers[i-1] + numbers[i-2])

print(numbers[n])